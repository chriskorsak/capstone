from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

class User(AbstractUser):
  pass

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=256)
  slug = models.SlugField(max_length=50, blank=True)
  body = RichTextField(blank=True, null=True)
  excerpt = models.TextField(max_length=512, blank=True)
  category = models.CharField(max_length=64, blank=True)
  premium = models.BooleanField(default=False)
  published = models.BooleanField(default=False)
  
  def __str__(self):
        return f"{self.author} {self.date} {self.title}"

class PostComment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  comment = models.CharField(max_length=256)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postComments")

  def __str__(self):
    return f"Date:{self.date} User:{self.user} Comment:{self.comment}"

class Feedback(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  video = models.URLField(max_length=200, blank=True)
  note = models.TextField(max_length=512)
  category = models.CharField(max_length=64, blank=True)

  def __str__(self):
    return f"User:{self.user} User:{self.video} Comment:{self.note}"

class FeedbackComment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  comment = models.CharField(max_length=256)
  feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name="feedbackComments")

  def __str__(self):
    return f"Date:{self.date} User:{self.user} Comment:{self.comment}"
