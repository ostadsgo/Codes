from django.shortcuts import render


def show_home(request):
    name = "bob"
    return render(request, "home.html", context={"name": name})
