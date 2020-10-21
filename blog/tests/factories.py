from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile, TemporaryUploadedFile

import factory
from factory.django import DjangoModelFactory

from ..models import BlogPost


class SuperUserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Sequence(lambda n: 'admin{}@admin.com'.format(n))
    username = factory.Sequence(lambda n: 'admin_{}'.format(n))
    password = 'passwd123'

    is_superuser = True
    is_staff = True
    is_active = True


class BlogPostFactory(DjangoModelFactory):
    class Meta:
        model = BlogPost
        django_get_or_create = ('title', 'content')

    title = "Hello World"
    subtitle = "Programming for starters"
    content = "Some content"
    author = factory.SubFactory(SuperUserFactory)


class BlogPostFileFactory(DjangoModelFactory):
    class Meta:
        model = BlogPost

    file = TemporaryUploadedFile(
        name="content.md",
        size=b"# title \n\n# subtitle1\n\nThis is a short paragraph!",
        charset='UTF-8',
        content_type='text/markdown',
    )
