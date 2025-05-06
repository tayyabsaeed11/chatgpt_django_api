import os, requests
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.utils import timezone
from .serializers import RegisterSerializer, ChatSerializer
from django.contrib.auth.models import User
from core.models import UserProfile
from rest_framework_simplejwt.views import TokenObtainPairView

OPENAI_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_URL = 'https://openrouter.ai/api/v1/chat/completions'

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

class ChatView(generics.GenericAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.reset_if_needed()

        if not profile.premium and profile.daily_count >= 5:
            reset_in = (profile.last_reset + timezone.timedelta(days=1)) - timezone.now()
            return Response({
                'detail': 'Daily free quota exhausted.',
                'reset_in_hours': round(reset_in.total_seconds() / 3600, 2),
                'upgrade': 'Purchase premium to lift limits.'
            }, status=status.HTTP_429_TOO_MANY_REQUESTS)

        prompt = request.data.get('prompt')
       
        headers = {'Authorization': f'Bearer {OPENAI_KEY}'}
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [{'role':'user','content': prompt}]
        }
        r = requests.post(OPENAI_URL, json=data, headers=headers)
        if r.status_code != 200:
            return Response(r.json(), status=r.status_code)

        
        if not profile.premium:
            profile.daily_count += 1
            profile.save()

        return Response(r.json(), status=status.HTTP_200_OK)
