import os
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


def avatar_path(instance, imagename):
    dir_path = 'account/images/'
    name = uuid.uuid4().hex
    extension = '.'+str(instance.avatar).split('.')[-1]
    return os.path.join(dir_path, name+extension)


class CustomUserModel(AbstractUser):
    """docstring for CustomUserModel.AbstractUser"""

    avatar = models.ImageField(upload_to=avatar_path, blank=True, null=True)

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = "Kullanıcılar"

    def __str__(self):
        text = f"id:{self.id}, username: {self.username}"
        return text
