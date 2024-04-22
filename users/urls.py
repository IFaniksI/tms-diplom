from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('report/', views.report, name='report'),
]