from django.http import HttpResponse

from .forms import CreateUserForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404

from users.models import Profile, Permission
from gyms.models import Subscription

from datetime import timedelta, date
from django.contrib import messages


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


@login_required
def update_profile(request):
    '''
    profile = request.user.profile

    if request.method == 'GET':
        return render(request, 'users/update_profile.html', {'profile': profile})

    if request.method == 'POST':
        username: str = request.POST.get('username')
        first_name: str = request.POST.get('first_name')
        last_name: str = request.POST.get('last_name')
        email: str = request.POST.get('email')

        profile.user.username = username
        profile.user.first_name = first_name
        profile.user.last_name = last_name
        profile.user.email = email
        profile.user.save()

        messages.success(request, 'Ваш профиль был успешно обновлен!')
        return redirect('users:profile')
    '''

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been successfully updated!')
        return redirect('users:profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        context = {'user_form': user_form}

    return render(request, 'users/update_profile.html', context=context)



















