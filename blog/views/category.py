from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from blog.models import PostModel, CategoryModel


def category(request, slug):
    category = get_object_or_404(CategoryModel, slug=slug)
    posts = category.c_post.filter(is_active=True).order_by('-id')
    search = request.GET.get('sq')
    if search:
        posts = posts.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search)
        ).distinct()
    page = request.GET.get('pg')
    paginator = Paginator(posts, 6)
    context={
        'category' : category.title,
        'posts' : paginator.get_page(page),
    }
    return render(request, 'category.html', context)
