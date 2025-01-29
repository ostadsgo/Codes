from django import forms
from django.contrib.auth.models import User
from .models import *
error = {
    'required':'این فیلد اجباری کسگم',
    'min_length': 'مترین ورودی باید 5',
    'invalid': 'ایمیلت نا معتبره دوست من'
}
class UserRegisterForm(forms.Form):
    user_name=forms.CharField(max_length=50,error_messages=error,widget=forms.TextInput(attrs={'placeholder': 'plz username'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'plz email'}),error_messages=error)
    first_name=forms.CharField(min_length=5,max_length=50,error_messages=error)
    last_name=forms.CharField(max_length=50)
    password_1=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'پسوورد رو وارد کن بچه کوچه ای'}))
    password_2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'پسوورد رو تکرار کن بچه کوچه ای'}))

    def clean_user_name(self):
        uuu = self.cleaned_data['user_name']
        if User.objects.filter(username=uuu).exists():
            raise forms.ValidationError("user exist")
        if len(uuu) > 15:
            raise forms.ValidationError('password not match5555555555555555555555555')
        return uuu

    def clean_email(self):
        uuu = self.cleaned_data['email']
        if User.objects.filter(email=uuu).exists():
            raise forms.ValidationError("email exist")
        return uuu
    def clean_password_2(self):
        password1=self.cleaned_data['password_1']
        password2=self.cleaned_data['password_2']
        if password1 != password2:
            raise forms.ValidationError('password not match')
        elif len(password2)<8:
            raise forms.ValidationError('password is short')
        elif not any(x.isupper() for x in password2):
            raise forms.ValidationError("حداقل یکی رو بزرگ بزار")
        return password1
class Userloginfirm(forms.Form):
    user=forms.CharField()
    password=forms.CharField()
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['phone','address']
class PhoneForm(forms.Form):
    phone = forms.IntegerField()
class CodeForm(forms.Form):
    code = forms.IntegerField()


