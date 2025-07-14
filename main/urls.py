from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu_view, name='menu'), 
    path('gallery/', views.gallery_view, name='gallery'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact/' ,views.contact, name='contact'),
    path('organizations/', views.organizations, name='organizations'),
    path('cafe/', views.cafe_view, name='cafe'),
    
    
  
]