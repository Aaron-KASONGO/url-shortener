from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create', views.CreateUrlView.as_view(), name='create'),
    path('<str:code>', views.access, name='redirect'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
]
