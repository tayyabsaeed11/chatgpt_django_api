from django.urls import path
from .views import RegisterView, LoginView, ChatView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('chat/', ChatView.as_view(), name='chat'),
]
