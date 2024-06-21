from django.urls import re_path, include
from myApp import views

urlpatterns = [
    re_path(r"^inicio/", views.inicio, name='inicio'),
    re_path('accounts/', include('django.contrib.auth.urls')),
    re_path(r"register/", views.register, name='register'),
]