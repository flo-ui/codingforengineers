from django.contrib.auth import get_user_model
from django.urls import resolve, reverse

import pytest
from mixer.backend.django import mixer

from blog.models import BlogPost


class TestUrls:
    @pytest.mark.parametrize("view_name", ["index", "about", "contact", "post-list"])
    def test_function_based_urls(self, view_name):
        path = reverse('blog:' + view_name)
        assert resolve(path).view_name == 'blog:' + view_name

    @pytest.mark.django_db
    def test_post_detail_url(self):
        user = mixer.blend(get_user_model())
        post = mixer.blend(BlogPost, slug='best-blog')
        path = reverse('blog:post-detail', kwargs={'slug': 'best-blog'})
        assert resolve(path).view_name == 'blog:post-detail'
