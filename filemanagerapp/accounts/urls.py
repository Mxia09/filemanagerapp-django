from django.urls import path
from accounts.views import home

urlpatterns = [
    # path("login/", user_login, name="login"),
    path("/", home, name="home")
]