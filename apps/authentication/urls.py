# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from .views import profile_upload, dependantfield

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('dependantfield', dependantfield, name="dependantfield"),
    path('dependantfield/hello', profile_upload, name="profile_upload"),
]
