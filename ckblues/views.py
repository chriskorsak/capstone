from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator

from .models import *

### VIEWS

def index(request):
  # all posts: create blank dict for storing categories and post counts with that category
  allCategories = {}
  allPosts = Post.objects.filter(published=True).order_by('category')
  # iterate through posts and add category if not in dict, or increment if already in dict
  for post in allPosts:
    if post.category not in allCategories:
      allCategories[post.category] = 1
    else:
      allCategories[post.category] += 1

  # free posts: create blank dict for storing categories and post counts with that category
  freeCategories = {}
  freePosts = Post.objects.filter(published=True).filter(premium=False).order_by('category')
  # iterate through posts and add category if not in dict, or increment if already in dict
  for post in freePosts:
    if post.category not in freeCategories:
      freeCategories[post.category] = 1
    else:
      freeCategories[post.category] += 1

  return render(request, "ckblues/index.html", {
  "freePosts": Post.objects.filter(published=True).filter(premium=False).order_by('-date'),
  "allPosts": Post.objects.filter(published=True).order_by('-date'),
  "allCategories": allCategories,
  "freeCategories": freeCategories
  })

def filterCategory(request, category):
  print(category)
  return render(request, "ckblues/index.html", {
  "freeFilteredPosts": Post.objects.filter(category=category).filter(published=True).filter(premium=False).order_by('-date'),
  "allFilteredPosts": Post.objects.filter(category=category).filter(published=True).order_by('-date')
  })

def post(request, slug):
  # get post
  post = Post.objects.get(slug=slug)
  # get all comments associated with post
  comments = PostComment.objects.filter(post=post)

  return render(request, "ckblues/post.html", {
    "post": post,
    "comments": comments
  })

@login_required
def postComment(request, postId):
  # get form input and user
  commentText = request.POST["comment"]
  user = request.user

  post = Post.objects.get(pk=postId)

  #create new Comment object with comment text, postId, and user
  comment = PostComment(user=user, comment=commentText, post=post)
  #save comment to database
  comment.save()

  return HttpResponseRedirect(reverse("post", args=(post.slug,)))

def register(request):
  if request.method == "POST":
    # get form inputs
    firstname = request.POST["first-name"]
    lastname = request.POST["last-name"]
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
      user.first_name = firstname
      user.last_name = lastname
      user.save()
    except IntegrityError:
      return render(request, "ckblues/register.html", {
        "message": "Username already taken."
      })
    # log in user after registration
    login(request, user)
    return HttpResponseRedirect(reverse("dashboard", args=(username,)))

  else:
    return render(request, "ckblues/register.html")

def loginView(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse("dashboard", args=(username,)))
    else:
      return render(request, "ckblues/login.html", {
      "message": "Invalid username and/or password."
      })
  else:
    return render(request, "ckblues/login.html")

def logoutView(request):
  logout(request)
  return HttpResponseRedirect(reverse("index"))

def dashboard(request, username):
  return render(request, "ckblues/dashboard.html", {
    "username": username
  })

def updateCredentials(request, username):
  if request.method == "POST":
    # get form inputs
    email = request.POST["email"]
    password = request.POST["password"]
    confirmation = request.POST["confirmation"]
    
    #get user object
    user = User.objects.get(username=username)

    if password and confirmation:
      # make sure passwords match
      if password != confirmation:
        return render(request, "ckblues/index.html", {
          "message": "New passwords must match."
        })
      else:
        #update password
        user.set_password(password)
    
    if email:
      user.email = email

    #save any email and/or password updates
    user.save()
  return HttpResponseRedirect(reverse("login"))


def feedback(request):
  return render(request, "ckblues/feedback.html")

