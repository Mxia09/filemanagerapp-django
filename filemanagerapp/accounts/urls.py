from django.urls import path
from accounts.views import user_login

urlpatters = [
    path("login/", user_login, name="login"),
]