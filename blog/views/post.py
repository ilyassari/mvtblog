import os
import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from blog.models import PostModel, CommentModel, CategoryModel
from blog.forms import AddPostForm, UpdatePostForm, AddCommentForm

def post(request, slug):
    """ viewing post detail """
    post = get_object_or_404(PostModel, slug=slug)
    comments = post.p_comments.all()
    if request.method == 'POST':
        comment_form = AddCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = CommentModel()
            new_comment.author = request.user
            new_comment.post = post
            new_comment.content = comment_form.cleaned_data['content']
            new_comment.save()
        if request.user.is_authenticated:
            logger = logging.getLogger('comment_added')
            logger.info(f'post-slug: {post.slug}, user: {request.user.username}')
        messages.success(request, 'Yeni yorum eklendi.')
        return redirect('post_url', slug=post.slug)
    else:
        comment_form = AddCommentForm()
    context={
        'post' : post,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    if request.user.is_authenticated:
        logger = logging.getLogger('post_viewed')
        logger.info(f'post-slug: {slug}, user: {request.user.username}')
    return render(request, 'post.html', context)


@staff_member_required(login_url='/')
def add_post(request):
    """ adding new post """
    form = AddPostForm(request.POST or None, request.FILES or None)
    print('\n\n')
    print('method', request.method)
    if request.method == "POST":
        print('post')
        form = AddPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_post = PostModel()
            new_post.title = cd['title']
            new_post.image = request.FILES['image']
            new_post.author = request.user
            new_post.content = cd['content']
            new_post.save()
            for id in cd['categories']:
                category = CategoryModel.objects.get(id=id)
                new_post.categories.add(category)
            messages.success(request, 'Yeni gönderi eklendi.')
            if request.user.is_authenticated:
                logger = logging.getLogger('post_added')
                logger.info(f'post-slug: {new_post.slug}, user: {request.user.username}')
            return redirect('post_url', slug=new_post.slug)
    context = {
        'form' : form,
    }
    return render(request, 'add_post.html', context)


@staff_member_required(login_url='/')
def update_post(request, slug):
    """ updating old post """
    print(request.GET)
    post = get_object_or_404(PostModel, slug=slug, author=request.user)
    initial = {
        'title' : post.title,
        'image' : post.image,
        'content' : post.content,
    }
    post_categories = CategoryModel.objects.filter(c_post=post)
    initial['categories'] = list(category.id for category in post_categories)
    form = UpdatePostForm(
        request.POST or None,
        request.FILES or None,
        initial=initial
    )
    if request.method == "POST":
        if form.is_valid():
            cd = form.cleaned_data
            post.title = cd['title']
            if request.FILES:
                if post.image:
                    os.remove(post.image.path)
                post.image = request.FILES['image']
            post.content = cd['content']
            post.categories.clear()
            for id in cd['categories']:
                category = CategoryModel.objects.get(id=id)
                post.categories.add(category)
            post.save()
            messages.success(request, 'Gönderi başarıyla güncellendi.')
            if request.user.is_authenticated:
                logger = logging.getLogger('post_updated')
                logger.info(f'post-slug: {slug}, user: {request.user.username}')
            return redirect('post_url', slug=post.slug)
    context = {
        'post' : post,
        'form' : form,
    }
    return render(request, 'update_post.html', context)


@staff_member_required(login_url='/')
def delete_post(request, slug):
    """ deleting a post """
    post = get_object_or_404(PostModel, slug=slug, author=request.user).delete()
    messages.success(request, 'Gönderi başarıyla silindi.')
    if request.user.is_authenticated:
        logger = logging.getLogger('post_deleted')
        logger.info(f'post-slug: {slug}, user: {request.user.username}')
    return redirect('my_posts_url')
