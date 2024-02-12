from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('list/', views.list_users, name='list_users'),
    path('add/', views.AddUserView.as_view(), name='add_user'),
]
