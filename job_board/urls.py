from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('job/<int:pk>/', views.job_detail, name='job-detail'),
]
