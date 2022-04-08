import uuid
import os

from django.contrib import admin
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

from account.models import CustomUserModel as User
from blog.models import CategoryModel


def image_path(instance, imagename):
    dir_path = 'blog/images/'
    name = uuid.uuid4().hex
    extension = '.'+str(instance.image).split('.')[-1]
    return os.path.join(dir_path, name+extension)

class PostModel(models.Model):
    """docstring for PostModel.
        Post substitute for Article
    """
    title = models.CharField(max_length=30, blank=False, null=False)
    image = models.ImageField(upload_to=image_path, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='a_post')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='c_post')
    content = RichTextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Gönderi"
        verbose_name_plural = "Gönderiler"

    @admin.display(boolean=True)
    def is_updated(self):
        return any((
            self.created_date.year != self.modified_date.year,
            self.created_date.month != self.modified_date.month,
            self.created_date.day != self.modified_date.day,
            self.created_date.minute != self.modified_date.minute,
            self.created_date.second != self.modified_date.second
        ))

    def category_list(self):
        categories = str()
        for category in self.categories.all():
            categories += category.title
            categories += ', '
        return categories.strip(', ')

    @admin.display(description='Author')
    def username(self):
        return self.author.username

    def __str__(self):
        text = f"id:{self.id}, title: {self.title}"
        return text
