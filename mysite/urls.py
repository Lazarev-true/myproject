from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mysite'),
    path('about/', views.about, name='about_page'),
]