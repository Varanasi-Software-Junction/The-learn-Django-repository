from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Book Home")


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
    # return logout(request)
    return HttpResponse("Logout")


def onlyloggedin(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return HttpResponse("Logged In" + str(request.user))
    return HttpResponse("Not Logged In")
