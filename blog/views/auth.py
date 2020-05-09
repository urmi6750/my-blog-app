from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.views import View

from django.db import transaction
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    FormView,
    TemplateView,
    View,
)
from blog import forms
from blog.forms.forms import UserUpdateForm, ProfileUpdateForm


class Registration(FormView):
    template_name = "blog/register.html"
    form_class = forms.Registration

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'account created successfully')
            return self.form_valid(form)

        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('SignUpDone')


class SignUpDone(TemplateView):
    template_name = 'blog/signupdone.html'


class Login(FormView):
    template_name = 'blog/login.html'
    form_class = forms.LoginForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)

            if user:
                login(request, user)
                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return self.form_valid(form)

            return self.form_invalid(form)

        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('Home')


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('Home'))


class Profile(View):
    template_name = 'blog/profile.html'
    form = UserUpdateForm
    profile_form = ProfileUpdateForm

    def post(self, request):
        user_form = self.form(request.POST)
        profile_form = self.profile_form(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            print(profile.user)
            profile.save()

            return render(request, self.template_name)
        else:
            return render(request, self.template_name, {'user_form': self.form,
                                                        'profile_form': self.profile_form})

    def get(self, request):
        if self.request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, self.template_name, {'user_form': self.form, 'profile_form': self.profile_form})

