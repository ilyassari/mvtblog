from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from blog.models import PostModel, CommentModel

def home(request):
    posts = PostModel.objects.filter(is_active=True).order_by('-id')
    search = request.GET.get('sq')
    if search:
        posts = posts.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search)
        ).distinct()
    if len(posts) > 3:
        page = request.GET.get('pg')
        paginator = Paginator(posts[1::], 6)
        context = {
            'featured' : posts[0],
            'posts' : paginator.get_page(page)
        }
    else:
        context = {
            'posts' : posts,
        }
    return render(request, "home.html", context)
