from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogPostLabel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)
    usage_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    author = models.ForeignKey(User, default=1,null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    labels = models.ManyToManyField(BlogPostLabel)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.content[:50]

    