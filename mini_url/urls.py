from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create_url, name='create'),
    path('<str:code>', views.access, name='redirect'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
]
