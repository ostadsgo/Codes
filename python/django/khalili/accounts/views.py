from django.shortcuts import render,redirect
from .forms import *
from kavenegar import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
import requests
from django.contrib.auth import update_session_auth_hash
from random import randint
import ghasedakpack
from django.contrib.auth.decorators import login_required
def user_register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=User.objects.create_user(username=data['user_name'],email=data['email'],
                                          first_name=data['first_name'],
                                          last_name=data['last_name'],password=data['password_2'])
            messages.success(request, 'register is ok', 'primary')
            user.save()
            return redirect('home:home')
        else:
            messages.error(request,'not ok','danger')

    else:
        form = UserRegisterForm()
    return render(request,'accounts/register.html',{'form':form})
def user_login(request):
    if request.method == 'POST':
        form =Userloginfirm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            try:
                user=authenticate(request,username = User.objects.get(email=data['user']),password=data['password'])
            except:
                user=authenticate(request,username=data['user'],password=data['password'])
            if user is not None:
                login(request,user)
                messages.success(request, 'login is ok','primary')
                return redirect('home:home')
            else:
                messages.error(request,'user or password is wrong','danger')

    else:
        form =Userloginfirm()
    return render(request,'accounts/login.html',{'form':form})
def user_logout(request):
    logout(request)
    messages.success(request,'logout is ok','danger')
    return redirect('home:home')

@login_required(login_url='accounts:login')
def user_profile(request):
    ppprofile = Profile.objects.get(user_id=request.user.id)
    return render(request,'accounts/profile.html',{'profile':ppprofile})
@login_required(login_url='accounts:login')
def user_update(request):
    if request.method =='POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if user_form and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'update is ok','success')
            return redirect('accounts:profile')
    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'user_form':user_form,'profile_form':profile_form}
    return render(request,'accounts/update.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'پسوورد با موفقیت تغییر کرد','success')
            return redirect('accounts:profile')
        else:
            messages.error(request,'سوورد درست نیست','success')

    else:
        form = PasswordChangeForm(request.user)
    return render(request,'accounts/change.html',{'form':form})
def phone(request):
    if request.method=="POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            global random_code
            data = form.cleaned_data
            phone = f"0{data['phone']}"
            random_code = randint(100,1000)
            api = KavenegarAPI(
                '6977386573716E684C564D714243685745676244775846303331487A55715948776C496259304B566566413D')
            params = {'sender': '1000689696', 'receptor': '09338995771', 'message': random_code}
            response = api.sms_send(params)
            return redirect('accounts/verify')

    else:
        form = PhoneForm()
    return render(request,'accounts/phone.html', {'form': form})

def verify(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if random_code == data['code']:
                profile = Profile.objects.get(phone=phone)
                user = User.objects.get(profile__id = Profile.id)
                login(request,user)
                messages.success(request,'hi user')
                return redirect('home:home')
            else:
                messages.error(request,'کدت غلطه')
    else:
        form = CodeForm()
    return render(request,'accounts/code.html',{'form':form})


