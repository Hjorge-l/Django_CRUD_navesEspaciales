from django.urls import re_path, include
from myApp import views
from myApp.naves.views import insert_data, show_all_data

urlpatterns = [
    re_path(r"^inicio/", views.inicio, name='inicio'),
    re_path('accounts/', include('django.contrib.auth.urls')),
    re_path(r"^register/", views.register, name='register'),
    re_path(r"^insert_data/", insert_data, name='insert_data'),
    re_path(r"^show_all_data/", show_all_data, name='show_all_data'),
]