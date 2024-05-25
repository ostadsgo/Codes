from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import RoomForm
from .models import Room, Topic


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist as e:
            messages.error(request, "User doesn not exist.")
            return redirect("login")
        else:
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "username or password is incorrect.")
    context = {}
    return render(request, "base/login_register.html", context)

def logout_user(request):
    logout(request)
    return redirect("home")


def home(request):
    q = request.GET.get('q')
    if q is not None:
        rooms = Room.objects.filter(
                Q(topic__name__icontains=q)|
                Q(name__icontains=q)|
                Q(description__icontains=q)
                )
    else:
        rooms = Room.objects.all()
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {"rooms": rooms, "topics": topics, "room_count": room_count}
    return render(request, "base/index.html", context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "base/room.html", context)

def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

        
    context = {"form": form}
    return render(request, "base/room_form.html", context)

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/room_form.html", context)

def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    context = {"obj": room}
    return render(request, "base/delete.html", context)
