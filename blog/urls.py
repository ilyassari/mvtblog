from django.urls import path

from blog.views import (
        index, home, category,
        user_posts, my_posts, my_comments, comments_to_me,
        post, add_post, update_post, delete_post,
        delete_comment,
    )

urlpatterns = [
    path('', index),
    path('home', home, name='home_url'),
    path('category/<slug:slug>', category, name='category_url'),
    path('user_posts/<int:id>', user_posts, name='user_posts_url'),
    path('my_posts', my_posts, name='my_posts_url'),
    path('my_comments', my_comments, name='my_comments_url'),
    path('comments_to_me', comments_to_me, name='comments_to_me_url'),
    path('post/<slug:slug>', post, name='post_url'),
    path('add_post', add_post, name='add_post_url'),
    path('update_post/<slug:slug>', update_post, name='update_post_url'),
    path('delete_post/<slug:slug>', delete_post, name='delete_post_url'),
    path('delete_comment/<int:id>', delete_comment, name='delete_comment_url'),
    ]
