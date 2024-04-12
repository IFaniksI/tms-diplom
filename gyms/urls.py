from django.urls import path

from . import views

app_name = 'gyms'
urlpatterns = [
    path('', views.index, name='index'),
    path('hall/<int:hall_id>/', views.detail, name='detail'),
    path('trainer/<int:trainer_id>/', views.info, name='info'),
]