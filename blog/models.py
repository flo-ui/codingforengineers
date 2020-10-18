from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey(User, default=1,null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    tags = TaggableManager()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def snippet(self, snip_end, snip_start=0):
        """ get an excerpt of the posts content """
        return self.content[snip_start:snip_end]

    