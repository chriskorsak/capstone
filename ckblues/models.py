from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  pass

class Post(models.Model):
  creator = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=64)
  
  ### need to figure out rich text editor for this field
  text = models.TextField()

  category = models.CharField(max_length=64, blank=True)
  status = models.BooleanField(default=False)
  
  def __str__(self):
        return f"{self.creator} {self.date} {self.likes}"

class PostComment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  comment = models.CharField(max_length=256)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postComments")

  def __str__(self):
    return f"Date:{self.date} User:{self.user} Comment:{self.comment}"

class Feedback(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  video = models.URLField(max_length=200, blank=True)
  comment = models.CharField(max_length=256)

  def __str__(self):
    return f"User:{self.user} User:{self.video} Comment:{self.comment}"

class FeedbackComment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  comment = models.CharField(max_length=256)
  feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name="feedbackComments")
