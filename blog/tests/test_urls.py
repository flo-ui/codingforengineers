import pytest
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from django.urls import reverse, resolve

from blog.models import BlogPost,BlogPostLabel


class TestUrls:

    @pytest.mark.parametrize("view_name", [
        "index",
        "about",
        "contact",
        "post-list"
    ])
    def test_function_based_urls(self, view_name):
        path = reverse('blog:' + view_name)
        assert resolve(path).view_name == 'blog:' + view_name

    @pytest.mark.django_db
    def test_post_detail_url(self):
        user = mixer.blend(User)
        label = mixer.cycle(3).blend(BlogPostLabel)
        post = mixer.blend(BlogPost, slug='best-blog')
        path = reverse('blog:post-detail', kwargs={'slug': 'best-blog'})
        assert resolve(path).view_name == 'blog:post-detail'
