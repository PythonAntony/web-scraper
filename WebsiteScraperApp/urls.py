from .import views
from django.urls import path

urlpatterns = [
    path("", views.home,name="home"),
    path('delete_all_records', views.delete_all_records, name='delete_all_records'),
]