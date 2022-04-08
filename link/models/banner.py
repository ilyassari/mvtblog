import uuid
import os

from django.db import models

def image_path(instance, imagename):
    dir_path = 'banners/images'
    name = uuid.uuid4().hex
    extension = '.'+str(instance.image).split('.')[-1]
    return os.path.join(dir_path, name+extension)

class BannerModel(models.Model):
    """docstring for BannerModel."""
    title = models.CharField(max_length=30, blank=False, null=False)
    image = models.ImageField(upload_to=image_path)
    url = models.CharField(max_length=260, blank=True, null=True, default="#/")
    description = models.TextField(max_length=400)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlar"

    def __str__(self):
        text = f"id:{self.id}, title: {self.title}"
        return text
