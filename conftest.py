import shutil

from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.test import override_settings

import pytest
from mixer.backend.django import mixer

from blog.models import BlogPost

TEST_DIR = "test_data"

""" Can be reimplemented with refactoring
@pytest.fixture
@override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
def file_test():
    print("Setup")
    yield
    print("\nDeleting temporary files...\n")
    try:
        shutil.rmtree(TEST_DIR)
    except OSError:
        pass
"""


@pytest.fixture
def lorem_post():
    post = BlogPost.objects.create(
        author=mixer.blend(get_user_model()),
        title="Lorem ipsum is awesome!",
        subtitle="The best nonsense",
        content="""Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim, quod, eum fuga obcaecati 
        eligendi doloremque sed ea dicta harum accusantium et, voluptas sint facere rem. Tempora pariatur commodi cum nobis.""",
        file=None,
    )
    return post
