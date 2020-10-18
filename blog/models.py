from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager

from .validators import validate_file_type

# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey(
        get_user_model(), default=1, null=True, on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    file = models.FileField(
        upload_to='uploads/', validators=[validate_file_type], blank=True, null=True
    )

    tags = TaggableManager(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def snippet(self, snip_end, snip_start=0):
        """ get an excerpt of the posts content """
        return self.content[snip_start:snip_end]
