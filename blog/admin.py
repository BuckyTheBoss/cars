from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)

class CommentInline(admin.StackedInline):
        model = Comment
        extra = 4

class PostAdmin(admin.ModelAdmin):
      
        fieldsets = [
            ('Post Data',               {'fields': ['title','content']}),
            ('User selection', {'fields': ['author']}),
        ]
        inlines = [CommentInline]

admin.site.register(Post, PostAdmin)