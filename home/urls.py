from django.urls import path
from home import views
from .views import tiles_view
from .views import marbles_view


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('tiles/', views.service, name='tiles'),
    path('contact/', views.contact_view, name='contact'),  
    path('/tiles/', tiles_view, name='tiles'),
    path('/marbles/', marbles_view, name='marbles'),
]
