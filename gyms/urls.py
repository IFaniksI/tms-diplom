from django.urls import path

from . import views

app_name = 'gyms'
urlpatterns = [
    path('', views.gyms, name='gyms'),
    path('<int:gym_id>/', views.gyms_details, name='gyms_details'),
    path('trainer/', views.trainer, name='trainer'),
    path('trainer/<int:trainer_id>/', views.trainer_details, name='trainer_details'),
    path('service/', views.service, name='service'),
    path('<int:gym_id>/service/<int:service_id>/', views.service_details, name='service_details'),
    path('<int:gym_id>/service/<int:service_id>/subscription/<int:subscription_id>/', views.subscription_view, name='subscription_view'),
    path('subscription_trainer/<int:trainer_id>/', views.subscription_trainer, name='subscription_trainer'),
]
