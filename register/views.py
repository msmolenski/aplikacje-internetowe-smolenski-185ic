from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PasswordsChangeView(PasswordChangeView):
	from_class = PasswordChangeForm
	success_url = reverse_lazy('password_success')
	
class Home(TemplateView):
    template_name = 'registration/login.html'

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
		return redirect("/")
	else:
		form = RegisterForm()

	return render(response, "register/register.html", {"form":form})

def password_success(request):
	return render(request, "edit_profile/password_success.html", {})

def loggedout(request):
	return render(request, "registration/loggedout.html", {})

def profile(response):
	return render(response, "edit_profile/profile.html")

def password_edit(response):
	return render(response, "edit_profile/password_edit.html")