from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse, reverse_lazy
from taggit.managers import TaggableManager

from martor.models import MartorField
from .validators import validate_file_type

# Create your models here.


class BlogPost(models.Model):

    author = models.ForeignKey(get_user_model(), default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(unique=True)
    content = MartorField(blank=True, null=True)
    file = models.FileField(
        blank=True,
        upload_to='uploads/',
        validators=[validate_file_type],
    )

    tags = TaggableManager(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    is_from_file = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"slug": self.slug})
    

    def clean(self):
        if not ((self.title and self.content) or self.file):
            raise ValidationError("You need to specify to specify title and content ot file")

        # if self.title and self.content and self.file:
        #    raise ValidationError("You cannot specify a file and title+content")

        # if (self.title and self.content == None) or (self.title == None and self.content):
        #    raise ValidationError(" Title and content must both be filled or empty")

    def save(self, *args, **kwargs):
        if self.file and self.is_from_file == True:
            file_content = self.file.read().decode('utf-8').split("\n\n", 1)
            self.title = file_content[0].replace("# ", "")
            self.content = file_content[1]
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def snippet(self, snip_end, snip_start=0):
        """ get an excerpt of the posts content """
        return self.content[snip_start:snip_end]
