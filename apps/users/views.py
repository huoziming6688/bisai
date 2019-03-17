# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email
from .models import UserProfile, EmailVerifyRecord
from .forms import RegisterForm, LoginForm, UploadImageForm, EditForm, ImageUploadForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


class RegisterView(View):
    def post(self, request):
        register_form = RegisterForm()
        return render(request, 'index.html', {'register_form':register_form})

    def get(self, request):
        register_form = RegisterForm(request.GET)
        if register_form.is_valid():
            user_name = request.GET.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'existed.html', {})
            pass_word = request.GET.get('password', '')
            n_name = request.GET.get('name', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.nick_name = n_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_email(user_name, 'register')
            return render(request, 'send_success.html')
        else:
            return render(request, 'index.html', {'register_form': register_form})


# def login(request):
#     if request.method =='POST':
#         pass
#     elif request.method =='GET':
#         return render(request, 'index.html',{})

class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'index.html')


class LoginView(View):
    def post(self, request):
        return render(request, 'index.html', {})

    def get(self, request):
        login_form = LoginForm(request.GET)
        if login_form.is_valid():
            pass
            user_name = request.GET.get('email', '')
            pass_word = request.GET.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'user-profile.html')
                else:
                    return render(request, 'index.html', {'msg': '用户未激活！'})
            else:
                return render(request, 'index.html', {'msg': '用户名或密码错误！', 'login_form': login_form})
        else:
            return render(request, 'index.html', {'login_form': login_form})


class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class Show(View):
    # def post(self, request):
    #     return render(request, 'user-profile.html', {})
    def post(self, request):
        edit_form = ImageUploadForm(request.POST, request.FILES)
        if edit_form.is_valid():
            image = edit_form.cleaned_data['image']
            request.user.image = image
            fname = request.POST.get('first_name', '')
            request.user.first_name = fname
            lname = request.POST.get('last_name', '')
            request.user.last_name = lname
            mobile = request.POST.get('mobile', '')
            request.user.mobile = mobile
            about = request.POST.get('about', '')
            request.user.about = about
            password = request.POST.get('password', '')
            request.user.save()
            pass
        return render(request, 'user-profile.html', {'edit_form': edit_form})
        # return render(request, 'user-profile.html', {
#         #     'edit_form': edit_form,
# })





