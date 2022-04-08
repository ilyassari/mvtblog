
import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from blog.models import CommentModel

@login_required(login_url='/')
def delete_comment(request, id):
    """ deleting a comment """
    comment = get_object_or_404(CommentModel, id=id, )
    if comment.author == request.user or comment.post.author == request.user:
        comment.delete()
        messages.success(request, 'Yorum başarıyla silindi.')
        if request.user.is_authenticated:
            logger = logging.getLogger('comment_deleted')
            logger.info(f'post-slug: {comment.post.slug}, comment-id: {id}, user: {request.user.username}')
        return redirect('post_url', slug=comment.post.slug)
    return redirect('home_url')
