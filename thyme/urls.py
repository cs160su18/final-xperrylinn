from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('homepageSearchQuery/', views.homepageSearchQuery, name='homepageSearchQuery'),
]