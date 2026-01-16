from django.urls import path, include, re_path

from . import views

app_name = 'main'

urlpatterns = [
    path("", views.main, name="main"),
]

