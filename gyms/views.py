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


def trainer(request: HttpRequest):
    objects_list = Trainer.objects.all()
    paginator = Paginator(objects_list, 5)

    page = request.GET.get('page')
    objects = paginator.get_page(page)

    return render(request, 'gyms/trainer.html', {
        'trainer_list': objects})


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
    context = Subscription.objects.filter(service=service_id).order_by('subscription_period')
    return render(request, 'gyms/service_details.html', {
        'subscription_list': context})


@login_required
def subscription_view(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id)
    profile = request.user.profile

    today = date.today()
    next_month = today + relativedelta(months=1)
    test = date(next_month.year, next_month.month, next_month.day)

    permission = (Permission.objects.filter(profile=profile, service_name=subscription.service.name).first()
                  or Permission.objects.create(profile=profile, service_name=subscription.service.name,
                                               subscription_end_date=date.today()))

    match subscription.subscription_period:
        case 7:
            permission.subscription_end_date += relativedelta(days=7)
        case 30:
            permission.subscription_end_date += relativedelta(months=1)
        case 180:
            permission.subscription_end_date += relativedelta(months=6)
        case 360:
            permission.subscription_end_date += relativedelta(months=12)
    permission.save()

    messages.success(
        request, f'Вы успешно продлили абонемент: {subscription.service.name}')

    return redirect('users:profile')
