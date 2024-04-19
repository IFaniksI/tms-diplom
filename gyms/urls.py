from django.urls import path

from . import views

app_name = 'gyms'
urlpatterns = [
    path('', views.gyms, name='gyms'),
    path('hall/<int:gym_id>/', views.gyms_details, name='gyms_details'),
    path('trainer/', views.trainer, name='trainer'),
    path('trainer/<int:trainer_id>/', views.trainer_details, name='trainer_details'),
    path('service/', views.service, name='service'),
    path('service_details/', views.service_details, name='service_details'),
    path('subscription_view/<int:subscription_id>/', views.subscription_view, name='subscription_view'),
]