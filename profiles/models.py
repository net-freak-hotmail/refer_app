from django.db import models
from django.contrib.auth.models import User
from .utils import generate_ref_code

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='referral_code')
    bio = models.TextField(blank=True)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='ref_by')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.code}"

    def get_recommend_profiles(self):
        return Profile.objects.filter(recommended_by=self.user)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_ref_code()
        super().save(*args, **kwargs)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    created_by = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_tasks', blank=True)

    def __str__(self):
        return self.title
