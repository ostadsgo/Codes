from django.http import HttpResponse
from django.template import loader

from .models import Member


def members(request):
    template = loader.get_template("all_members.html")
    all_memebers = Member.objects.all()
    context = {"members": all_memebers}
    return HttpResponse(template.render(context, request))


def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {"member": member}
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template("template.html")
    context = {"fruites": ["Apple", "Banana", "Cherry"]}
    return HttpResponse(template.render(context, request))
