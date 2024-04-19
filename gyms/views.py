from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from gyms.models import *

from users.models import *
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta

from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def gyms(request: HttpRequest):
    search_query = request.GET.get('search', '')
    context = Gym.objects.filter(name__icontains=search_query) if search_query else Gym.objects.all()
    return render(request, 'gyms/gyms.html', {
        'gym_list': context})


def trainer(request: HttpRequest):
    context = Trainer.objects.all()
    return render(request, 'gyms/trainer.html', {
        'trainer_list': context})


def gyms_details(request, gym_id):
    return render(request, 'gyms/gyms_details.html', {
        'gym': get_object_or_404(Gym, id=gym_id)})


def trainer_details(request, trainer_id):
    return render(request, 'gyms/trainer_details.html', {
        'trainer': get_object_or_404(Trainer, id=trainer_id)})


def service(request: HttpRequest):
    context = Service.objects.all()
    return render(request, 'gyms/service.html', {
        'service_list': context})


def service_details(request: HttpRequest, service_id):
    context = Subscription.objects.filter(service=service_id)
    return render(request, 'gyms/service_details.html', {
        'subscription_list': context})


@login_required
def subscription_view(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id)
    profile = request.user.profile

    today = date.today()
    next_month = today + relativedelta(months=1)
    test = date(next_month.year, next_month.month, next_month.day)

    permission = Permission.objects.filter(service_name=subscription.service.name, profile=profile).first()
    if permission:
        permission.subscription_end_date += relativedelta(months=1) if subscription.subscription_period == 30 else relativedelta(days=7)
        permission.save()
    else:
        Permission.objects.create(profile=profile, service_name=subscription.service.name, subscription_end_date=test)

    messages.success(
        request, f'Вы успешно продлили абонемент: {subscription.service.name}')

    return redirect('users:profile')
