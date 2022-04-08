from django import template

from link.models import SocialLinkModel

register = template.Library()

@register.simple_tag
def social_tags():
    social_webs = SocialLinkModel.objects.all()
    return social_webs
