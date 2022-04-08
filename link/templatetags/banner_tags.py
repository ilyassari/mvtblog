from django import template

from link.models import BannerModel

register = template.Library()

@register.simple_tag
def banner_tags():
    banners = BannerModel.objects.all()
    return banners
