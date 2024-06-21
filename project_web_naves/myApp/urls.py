from django.urls import re_path, include
from myApp import views

urlpatterns = [
    re_path(r"^inicio/", views.inicio, name='inicio'),
    re_path(r"accounts/", include('django.contrib.auth.urls')),
]