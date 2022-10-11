from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .forms import StudentForm
from .models import BooksModel
from django.shortcuts import render

# Create your views here.

def studentview(request):
    return render(request, "student.html", {"form": StudentForm()})

def index(request):
    print(BooksModel.objects.all())
    output = serializers.serialize("json", BooksModel.objects.all())
    # return JsonResponse(output,safe=False)
    return HttpResponse(output, content_type="application/json")


def createUser(request):
    user = User.objects.create_user('popat', 'champak@gmail.com', 'champakpassword')
    user.save()
    return HttpResponse("Create")


def changepassword(request):
    user = User.objects.get(username='popat')
    user.set_password('newpassword')
    user.first_name = "Popat"
    user.last_name = "Lal"
    user.save()
    return HttpResponse("Password Changed")


def authenticateuser(request):
    user = authenticate(username='popat', password='newpassword')
    print(user)
    if user is not None:
        login(request, user)
        return HttpResponse(str(user))
    else:
        return HttpResponse("Login failed")


def dologout(request):
    logout(request)
    return HttpResponse("Logout")


def onlyloggedin(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return HttpResponse("Logged In" + str(request.user))
    return HttpResponse("Not Logged In")
