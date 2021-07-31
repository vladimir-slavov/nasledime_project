from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from nasledime_project.profiles.forms import RegisterForm


class RegisterUser(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            'form': form,
        }

        return render(request, 'profiles/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'profiles/register.html', context)
