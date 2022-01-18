from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('map/', views.index, name='index'),
    path('statistics/', views.statistics_page, name='statistics'),
]