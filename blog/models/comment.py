from django.db import models

from account.models import CustomUserModel as User
from blog.models import PostModel

class CommentModel(models.Model):
    """Gönderilere ilişkin yorumları içerir"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='a_comments')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='p_comments')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"

    def __str__(self):
        text = f"id:{self.id}, post: {self.post}"
        return text
