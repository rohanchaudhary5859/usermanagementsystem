from django.contrib import admin
from .models import User, Discussion, Comment, HashTag, Like

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'mobile_no']
    search_fields = ['username', 'email', 'mobile_no']
    list_filter = ['created_at']

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'created_on']
    search_fields = ['text']
    list_filter = ['created_on']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'discussion', 'created_on']
    search_fields = ['text']
    list_filter = ['created_on']

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'comment']
    search_fields = ['user__username', 'comment__text']
