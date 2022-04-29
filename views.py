from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    header = "Personal Data"
    user = {"name": "Михаил", "surname": "Леонов", "age": 21}

    data = {"header": header, "user": user, "people": Staff.objects.all()}
    return render(request, "index.html", context=data)
    # return render(request, "index.html", {"people": people})


# сохранение данных в бд
def Create(request):
    if request.method == "POST":
        person = Staff()
        person.name = request.POST.get("name")
        person.surname = request.POST.get("surname")
        person.position = request.POST.get("position")
        person.maritalStatus = request.POST.get("maritalStatus")
        person.education = request.POST.get("education")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        person = Staff.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.surname = request.POST.get("surname")
            person.position = request.POST.get("position")
            person.maritalStatus = request.POST.get("maritalStatus")
            person.education = request.POST.get("education")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Staff.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Staff.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Staff.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def TableView(request):
    return render(request, "table.html", {"tablets": Timetable.objects.all()})


def TableEdit(request, id):
    try:
        person = Timetable.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.position = request.POST.get("position")
            person.instruments = request.POST.get("instruments")
            person.DateTime = request.POST.get("DateTime")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "TableEdit.html", {"person": person})
    except Staff.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def AboutCompany(request):
    return render(request, "AboutCompany.html", {"about": Service.objects.all()})