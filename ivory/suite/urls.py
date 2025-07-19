from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name="home"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('rooms/', views.rooms,name="rooms"),
    path('reservation/', views.reservation,name="reservation"),
    path('events/', views.events,name="events"),
]