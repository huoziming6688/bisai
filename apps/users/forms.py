# _*_ encoding:utf-8 _*_
__author__ = '595'
__date__ = '2019/3/5 20:39'

from django import forms
from .models import UserProfile


class RegisterForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class EditForm(forms.Form):
    image = forms.FileField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    about = forms.CharField(required=True)
    password = forms.CharField(required=True)
    c_password = forms.CharField(required=True)


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['image', 'first_name', 'last_name', 'mobile', 'about']