from django.urls import path
from . import views


urlpatterns = [
    path('generate_file/<str:file_name>/<int:data_count>/', views.file, name='file' ),
]