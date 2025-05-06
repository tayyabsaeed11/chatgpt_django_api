from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    daily_count = models.IntegerField(default=0)
    last_api_request = models.DateTimeField(null=True, blank=True)
    premium = models.BooleanField(default=False)
    last_reset = models.DateTimeField(default=timezone.now)

    def reset_if_needed(self):
        if timezone.now() - self.last_reset >= timezone.timedelta(days=1):
            self.daily_count = 0
            self.last_reset = timezone.now()
            self.save()

    def can_make_request(self):
        self.reset_if_needed()
        return self.premium or self.daily_count < 5