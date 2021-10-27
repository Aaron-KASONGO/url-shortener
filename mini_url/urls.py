from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create', views.CreateUrlView.as_view(), name='create'),
    path('update/<str:code>', views.UpdateUrlView.as_view(), name='update'),
    path('delete/<str:code>', views.DeleteUrlView.as_view(), name='delete'),
    path('<str:code>', views.access, name='redirect'),
    path('register/', views.register, name='register'),
    path('signin/', views.Login.as_view(), name='signin'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('changepassword/', views.ChangePasswordView.as_view(), name='changepassword'),
    path('changepassword-done', views.PasswordDone.as_view(), name='password_done')
]
