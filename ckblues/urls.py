from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<str:category>", views.filterCategory, name="filterCategory"),
    path("post/<str:slug>", views.post, name="post"),
    path("postComment/<int:postId>", views.postComment, name="postComment"),
    path("register", views.register, name="register"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path("dashboard/<str:username>", views.dashboard, name="dashboard"),
    path("updatecredentials/<str:username>", views.updateCredentials, name="update-credentials"),
    path("feedback-form", views.feedbackForm, name="feedback-form"),
    path("feedback/<int:feedbackId>", views.feedback, name="feedback"),
    path("feedbackComment/<int:feedbackId>", views.feedbackComment, name="feedbackComment")
]

#check to make sure my naming conventions are consistent!!!!