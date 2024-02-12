from django.urls import path
from .views import CountData, index

urlpatterns = [
    path('query_builder/api/count_data/', CountData.as_view(), name='count_data_api'),
    path('', index, name='query_builder'),
]
