from django.http import HttpResponse

from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404

from users.models import Profile, Permission
from gyms.models import Subscription

from datetime import timedelta, date


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            Profile.objects.create(user=request.user)

            return redirect(request.GET.get("next", '/'))
    else:
        form = CreateUserForm()
    return render(request, 'registration/register.html', {"form": form})


@login_required
def profile(request):
    # profile: Profile = Profile.objects.get(user=request.user).first()
    profile = request.user.profile
    permission_1 = Permission.objects.filter(profile=profile, service_name='Тренажерный зал') \
        .order_by('-subscription_end_date') \
        .first()
    permission_2 = Permission.objects.filter(profile=profile, service_name='Кроссфит') \
        .order_by('-subscription_end_date') \
        .first()
    context = {'profile': profile, 'permission_1': permission_1, 'permission_2': permission_2}
    return render(request, 'users/profile.html', context)


















