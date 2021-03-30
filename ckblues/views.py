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
  if request.user.is_authenticated:
    posts = Post.objects.filter(published=True).order_by('-date')
  else:
    posts = Post.objects.filter(published=True).filter(premium=False).order_by('-date')

  paginator = Paginator(posts, 8) # Show 8 posts per page.
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  # exctract distinct list of blog post categories
  categories = {}
  # iterate through posts and add category if not in dict, or increment if already in dict
  for post in posts:
    if post.category not in categories:
      categories[post.category] = 1
    else:
      categories[post.category] += 1
  
  return render(request, "ckblues/index.html", {
  "categories": sorted(categories),
  'page_obj': page_obj
  })

def filterCategory(request, category):
  if request.user.is_authenticated:
    posts = Post.objects.filter(published=True).filter(category=category).order_by('-date')
  else:
    posts = Post.objects.filter(published=True).filter(premium=False).filter(category=category).order_by('-date')

  paginator = Paginator(posts, 8) # Show 8 posts per page.
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  return render(request, "ckblues/category.html", {
    "page_obj": page_obj,
    "category": category
  })

def post(request, slug):
  # get post
  post = Post.objects.get(slug=slug)
  # get all comments associated with post
  comments = PostComment.objects.filter(post=post).order_by('-date')

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

@login_required
def dashboard(request, username):
  user = request.user
  feedbacks = Feedback.objects.filter(user=user).order_by('-date')
  return render(request, "ckblues/dashboard.html", {
    "username": username,
    "feedbacks": feedbacks
  })

@login_required
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

@login_required
def feedbackForm(request):
  if request.method == "POST":
    # get user
    user = request.user
    # get form inputs
    video = request.POST["video-url"]
    category = request.POST["video-category"]
    note = request.POST["video-note"]
    
    #create and save new post using post model/object
    newFeedback = Feedback(user=user, video=video, category=category, note=note)
    newFeedback.save()
    #send user to newly created feedback page
    return HttpResponseRedirect(reverse("feedback", args=(newFeedback.id,)))

  return render(request, "ckblues/feedback-form.html")

@login_required
def feedback(request, feedbackId):
  user = request.user
  feedback = Feedback.objects.get(id=feedbackId)
  
  #reroute user if trying to access a feedback they didn't create
  if feedback.user != user:
    return render(request, "ckblues/feedback-form.html")

  #strip off parts of urls so I can reformat url in page later: ex https://youtu.be/yTZootAFRGw becomes yTZootAFRGw
  feedback.video = feedback.video[17:]
  if feedback.videoResponse:
    feedback.videoResponse = feedback.videoResponse[17:]

  # get all comments associated with feedback
  comments = FeedbackComment.objects.filter(feedback=feedback).order_by('-date')

  return render(request, "ckblues/feedback.html", {
    "feedback": feedback,
    "comments": comments
  })

@login_required
def feedbackComment(request, feedbackId):
  # get form input and user
  commentText = request.POST["comment"]
  user = request.user

  feedback = Feedback.objects.get(pk=feedbackId)

  #create new Comment object with comment text, feedbackId, and user
  comment = FeedbackComment(user=user, comment=commentText, feedback=feedback)
  #save comment to database
  comment.save()

  return HttpResponseRedirect(reverse("feedback", args=(feedbackId,)))


