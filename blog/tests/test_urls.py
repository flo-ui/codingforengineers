import pdb

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import resolve, reverse

import pytest

from blog.models import BlogPost

from .factories import BlogPostFactory, SuperUserFactory


class TestUrls:
    @pytest.mark.parametrize("view_name", ["index", "about", "contact", "post-list"])
    def test_function_based_urls(self, view_name):
        path = reverse('blog:' + view_name)
        assert resolve(path).view_name == 'blog:' + view_name

    @pytest.mark.django_db
    def test_post_detail_url(self):
        user = SuperUserFactory()

        post = BlogPostFactory()
        path = reverse('blog:post-detail', kwargs={'slug': 'best-blog'})
        assert resolve(path).view_name == 'blog:post-detail'
