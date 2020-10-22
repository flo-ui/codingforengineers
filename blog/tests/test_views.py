from django.contrib.auth.models import AnonymousUser
from django.http import request
from django.test import RequestFactory
from django.urls import resolve, reverse, reverse_lazy
from django.urls.base import reverse_lazy
from django.template import Template, Context
from .factories import BlogPostFactory

import pytest

from .. import views

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('view_name', ['index', 'about', 'contact'])
def test_static_pages(view_name, rf):
    url = reverse_lazy('blog:'+view_name)
    request = rf.get(url)
    request.user = AnonymousUser()
    response = resolve(url).func(request)
    assert response.status_code == 200, 'should be called by anyone'


def test_detail_view():
    template = Template("{% load markdown_extras %}{{ post.content|markdown|safe }}")
    post = BlogPostFactory(content="# extensive markdown test\n\n List: \n\n * one\n * two\n")
    rendered = template.render(Context({'post':post}))
    assert "<li>one</li>" in rendered