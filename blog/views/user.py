from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from blog.models import PostModel, CommentModel
from account.models import CustomUserModel


def user_posts(request, id):
    user = get_object_or_404(CustomUserModel, id=id)
    posts = user.a_post.order_by('-id')
    page = request.GET.get('pg')
    paginator = Paginator(posts, 6)
    context={
        'user' : user.username,
        'posts' : paginator.get_page(page),
    }
    return render(request, 'category.html', context)

@login_required(login_url='/blog/home')
def my_posts(request):
    posts = request.user.a_post.order_by('-id')
    page = request.GET.get('pg')
    paginator = Paginator(posts, 10)
    context={
        'posts': paginator.get_page(page),
    }
    return render(request, 'my_posts.html', context)

@login_required(login_url='/blog/home')
def my_comments(request):
    comments = request.user.a_comments.order_by('-id')
    page = request.GET.get('pg')
    paginator = Paginator(comments, 10)
    context={
        'comments': paginator.get_page(page),
        'description': 'Yaptığım Yorumlar'
    }
    return render(request, 'my_comments.html', context)

@login_required(login_url='/blog/home')
def comments_to_me(request):
    comments = CommentModel.objects.order_by('-id')
    comments= list(comment for comment in comments if comment.post.author == request.user)
    page = request.GET.get('pg')
    paginator = Paginator(comments, 10)
    context={
        'comments': paginator.get_page(page),
        'description': 'Bana Yapılan Yorumlar'
    }
    return render(request, 'my_comments.html', context)
