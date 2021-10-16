from django.urls import path
from . import views


urlpatterns = [ #routes for the urls
    path('' , views.home, name='blog-home'),#accessing the home method in views
    path('about/' , views.about, name='blog-about'),#accessing the about method in views
    path('cyclura/' , views.cyclura, name='blog-cyclura'),#accessing the cyclura method in views
    path('camry/' , views.camry, name='blog-camry'),#accessing the camry method in views
]
