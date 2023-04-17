import sys
import os
from decouple import config
from .forms import UserRegisterForm, UserUpdateForm
from .models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, ListView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            user = get_object_or_404(User, username=username)
            profile = get_object_or_404(Profile, user=user)
            profile.save()
            if form.cleaned_data.get('email'):
                return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


    points_leaders = Profile.objects.all().order_by("-points")
    context = {
        "points_leaders": points_leaders
    }
    return render(request, 'users/leaderboard.html', context=context)