from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.csv_read, name='read_csv'),
]
