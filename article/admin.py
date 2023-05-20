from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.

# 1-usul
# admin.site.register(Category)
# admin.site.register(Post)

# 2-usul
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id','status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields  = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'see', 'status','created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'subtitle', 'body')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','post','email', 'status','created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'body')


