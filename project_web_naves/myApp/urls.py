from django.urls import re_path, include
from myApp import views

urlpatterns = [
    re_path(r"^inicio/", views.inicio, name='inicio'),
]