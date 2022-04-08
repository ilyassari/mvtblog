from django.db import models
from django.contrib import admin

class SocialLinkModel(models.Model):
    """docstring for ContactModel.models.Model"""
    social_webs = (
        ('1', "Facebook"),
        ('2', "Twitter"),
        ('3', "Google"),
        ('4', "Instagram"),
        ('5', "Linkedin"),
        ('6', "Pinterest"),
        ('7', "Vkontakte"),
        ('8', "Stack overflow"),
        ('9', "Youtube"),
        ('10', "Slack"),
        ('11', "Github"),
        ('12', "Dribbble"),
        ('13', "Reddit"),
    )
    title = models.CharField(choices=social_webs, unique=True, max_length=2)
    url = models.URLField()

    class Meta:
        verbose_name = "Sosyal Ağ"
        verbose_name_plural = "Sosyal Ağlar"

    @admin.display(boolean=True)
    def fa_class(self):
        fa_classes = (
            '',
            'fa-facebook',
            'fa-twitter',
            'fa-google',
            'fa-instagram',
            'fa-linkedin',
            'fa-pinterest',
            'fa-vk',
            'fa-stack-overflow',
            'fa-youtube',
            'fa-slack',
            'fa-github',
            'fa-dribbble',
            'fa-reddit',
        )
        return fa_classes[int(self.title)]

    def __str__(self):
        text = f"id:{self.id}, title: {self.title}"
        return text
