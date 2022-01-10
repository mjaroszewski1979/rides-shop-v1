from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('expedition/', views.expedition, name='expedition'),
    path('racing/', views.racing, name='racing'),
    path('speed/', views.speed, name='speed'),
    path('vintage/', views.vintage, name='vintage'),
    path('cars/', views.cars, name='cars'),
    path('car/<slug:car_slug>/', views.car, name='car'),
    path('category/<slug:category_slug>/', views.category, name='category'),
]