from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_user),
    path("", all_users),
    path("<int:pk>/", get_user),
    path("<int:pk>/update/", update_user),
]  