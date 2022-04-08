from django.urls import path
from django.contrib.auth.views import LoginView

from account.views import sign_out, change_pwd, update_user, sign_up, sign_in


urlpatterns = [
    path('sign_up', sign_up, name='sign_up_url'),
    path('sign_in', sign_in, name='sign_in_url'),
    path('update_user', update_user, name='update_user_url'),
    path('change_pwd', change_pwd, name='change_pwd_url'),
    path('sign_out', sign_out, name='sign_out_url'),
    # path('profile/<str:username>', UserDetailView.as_view(), name='profile_url'),
]
