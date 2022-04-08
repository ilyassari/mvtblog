from django.db import models

class ContactModel(models.Model):
    """docstring for ContactModel.models.Model"""
    title = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    full_name = models.CharField(max_length=30)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "İletişim"
        verbose_name_plural = "İletişim"

    def __str__(self):
        text = f"id:{self.id}, title: {self.title}"
        return text
