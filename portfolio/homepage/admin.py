from django.contrib import admin
from blog.models import Blog, Post
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'created', 'blog')