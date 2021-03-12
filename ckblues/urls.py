from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path("dashboard/<str:username>", views.dashboard, name="dashboard"),
    path("setpassword/<str:username>", views.setPassword, name="set-password"),
    path("feedback", views.feedback, name="feedback")
]