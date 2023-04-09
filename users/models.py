from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    status = models.CharField(max_length=50, default='Available')

    picture = models.ImageField(
        upload_to='users/profile_pictures',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username
