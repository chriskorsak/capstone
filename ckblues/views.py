from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponse

### VIEWS

def register(request):
  if request.method == "POST":
    # get form inputs
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    confirmation = request.POST["confirmation"]

    # make sure passwords match
    if password != confirmation:
      return render(request, "ckblues/register.html", {
        "message": "Passwords must match."
      })

    # try to create new user
    try:
      user = User.objects.create_user(username, email, password)
      user.save()
    except IntegrityError:
      return render(request, "network/register.html", {
        "message": "Username already taken."
      })
    # log in user after registration
    login(request, user)
    return HttpResponseRedirect(reverse("index"))

  else:
    return render(request, "ckblues/register.html")

def login(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    print(username, password)
    user = authenticate(request, username=usernamme, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse("index"))
  else:
    return render(request, "ckblues/login.html")

def logout(request):
  logout(request)
  return HttpResponseRedirect(reverse("index"))

def index(request):
  return render(request, "ckblues/index.html")
