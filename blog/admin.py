from django.contrib import admin

from .models import BlogPost
from django.db import models
from martor.widgets import AdminMartorWidget
from martor.models import MartorField
# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'views']
    formfield_overrides = {
        MartorField: {'widget': AdminMartorWidget},
        models.TextField: {'widget': AdminMartorWidget},
    }

    #https://github.com/agusmakmun/django-markdown-editor/issues/12
    class Media:
        css = {'all': ('css/my-custom-ace.css', )}
admin.site.register(BlogPost, BlogPostAdmin)
