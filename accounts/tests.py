from django.contrib.auth import get_user_model
from django.test import TestCase

import pytest

# Create your tests here.


@pytest.mark.django_db
def test_create_superuser():
    User = get_user_model()
    user = User.objects.create_superuser(username='superadmin', email='superadmin@email.com', password='testpass123')

    assert str(user) == "superadmin"
