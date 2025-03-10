from django.urls import path
from interface.views import index

urlpatterns = [
    path("test/", index)
]