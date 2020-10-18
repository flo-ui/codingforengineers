from django.contrib.auth.models import AnonymousUser
from django.http import request
from django.test import RequestFactory
from django.urls import resolve, reverse, reverse_lazy
from django.urls.base import reverse_lazy

import pytest

from .. import views

pytestmark = pytest.mark.django_db


#class TestIndexView:
    #def test_index_view_status_code(self):
    #    path = reverse_lazy('blog:index')
    #    request = RequestFactory().get('')
    #    request.user = AnonymousUser()
    #    response = views.index(request)
    #    assert response.status_code == 200, 'should be called by anyone'
