from django.contrib import admin

# Register your models here.
from .models import BlogPost, BlogPostAdmin

admin.site.register(BlogPost, BlogPostAdmin)