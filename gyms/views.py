from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from gyms.models import Gym, Trainer


# Create your views here.
def index(request: HttpRequest):

    search_query = request.GET.get('search', '')

    context = Gym.objects.filter(name__icontains=search_query) if search_query else Gym.objects.all()

    return render(request, 'gyms/index.html', {
        'gym_list': context})


def detail(request, hall_id):
    return render(request, 'gyms/detail.html', {
        'gym': get_object_or_404(Gym, id=hall_id)})


def info(request, trainer_id):
    return render(request, 'gyms/info.html', {
        'trainer': get_object_or_404(Trainer, id=trainer_id)})