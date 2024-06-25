from django.urls import re_path, include
from myApp import views
from myApp.naves.views import (insert_data, show_all_data, search_by_id,
                               search_by_name, update_by_id, delete_by_id)

urlpatterns = [
    re_path(r"^inicio/", views.inicio, name='inicio'),
    re_path('accounts/', include('django.contrib.auth.urls')),
    re_path(r"^register/", views.register, name='register'),
    re_path(r"^insert_data/", insert_data, name='insert_data'),
    re_path(r"^show_all_data/", show_all_data, name='show_all_data'),
    re_path(r"^search_by_id/", search_by_id, name="search_by_id"),
    re_path(r"^search_by_name/", search_by_name, name="search_by_name"),
    re_path(r"^update_by_id/", update_by_id, name="update_by_id"),
    re_path(r"^delete_by_id/", delete_by_id, name="delete_by_id"),
]