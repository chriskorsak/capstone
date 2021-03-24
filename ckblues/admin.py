from django.contrib import admin

from . models import User, Post, PostComment, Feedback, FeedbackComment

class UserAdmin(admin.ModelAdmin):
  list_display = ("username", "first_name", "last_name", "email", "id")

class PostAdmin(admin.ModelAdmin):
  list_display = ("author", "date", "title", "category", "premium", "published")
  prepopulated_fields = {"slug": ("title",)}

class PostCommentAdmin(admin.ModelAdmin):
  list_display = ("user", "date", "comment", "post")

class FeedbackAdmin(admin.ModelAdmin):
  list_display = ("user", "date", "category")

class FeedbackCommentAdmin(admin.ModelAdmin):
  list_display = ("user", "date", "comment", "feedback")

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(FeedbackComment, FeedbackCommentAdmin)


