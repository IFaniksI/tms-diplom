from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from gyms.models import *

from users.models import *
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta

from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def gyms(request: HttpRequest):
    search_query = request.GET.get('search', '')
    context = Gym.objects.filter(Q(name__icontains=search_query) | Q(address__icontains=search_query)) if search_query \
        else Gym.objects.all()

    paginator = Paginator(context, 5)

    page = request.GET.get('page')
    objects = paginator.get_page(page)

    return render(request, 'gyms/gyms.html', {
        'gym_list': objects})


def gyms_details(request, gym_id):
    gym = Gym.objects.get(id=gym_id)
    service = gym.servicex.all()
    request.session["test"] = gym_id
    return render(request, 'gyms/gyms_details.html', {
        'gym': get_object_or_404(Gym, id=gym_id), 'service_list': service})


def trainer(request: HttpRequest):
    objects_list = Trainer.objects.all()
    paginator = Paginator(objects_list, 6)

    page = request.GET.get('page')
    objects = paginator.get_page(page)

    return render(request, 'gyms/trainer.html', {
        'trainer_list': objects})


def trainer_details(request, trainer_id):
    return render(request, 'gyms/trainer_details.html', {
        'trainer': get_object_or_404(Trainer, id=trainer_id)})


def service(request: HttpRequest):
    context = Service.objects.all()
    return render(request, 'gyms/service.html', {
        'service_list': context})


def service_details(request: HttpRequest, gym_id: int, service_id: int):
    service = Service.objects.get(id=service_id)
    x = service.aboniment.all()
    gym = Gym.objects.get(id=gym_id)
    return render(request, 'gyms/service_details.html', {
        'service_list': x, 'gym': gym})


@login_required
def subscription_view(request, gym_id: int, service_id: int, subscription_id: int):
    subscription = get_object_or_404(Subscription, id=subscription_id)
    profile = request.user.profile
    gym = Gym.objects.get(id=gym_id)

    permission = Permission.objects.create(profile=profile, service_name=subscription.service.name,
                                           subscription_name=subscription.name, gym_name=gym.name,
                                           start_date=date.today(), end_date=date.today())

    match subscription.subscription_period:
        case 7:
            permission.end_date += relativedelta(days=7)
        case 30:
            permission.end_date += relativedelta(months=1)
        case 180:
            permission.end_date += relativedelta(months=6)
        case 360:
            permission.end_date += relativedelta(months=12)
    permission.save()

    messages.success(
        request, f'Вы успешно продлили абонемент: {subscription.service.name}')

    return redirect('users:profile')



@login_required
def subscription_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    profile = request.user.profile

    permission = Permission.objects.create(profile=profile, service_name='Персональные тренировки',
                                           subscription_name= f'{trainer.first_name} {trainer.last_name}',
                                           gym_name=trainer.gym.name,
                                           start_date=date.today(), end_date=date.today())

    permission.end_date += relativedelta(days=7)
    permission.save()

    messages.success(
        request, f'Вы успешно продлили абонемент')

    return redirect('users:profile')