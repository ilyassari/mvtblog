from django import template

from blog.models import CategoryModel

register = template.Library()

@register.simple_tag
def category_tags():
    categories = CategoryModel.objects.all()
    return categories
