from django.contrib import admin
from .models import BlogPost, BlogPostLabel

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogPostLabel)