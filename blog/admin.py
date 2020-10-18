from django.contrib import admin

from .models import BlogPost

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'views']


admin.site.register(BlogPost, BlogPostAdmin)
