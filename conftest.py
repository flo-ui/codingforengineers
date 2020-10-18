from django.contrib.auth import get_user_model

import pytest
from mixer.backend.django import mixer

from blog.models import BlogPost


@pytest.fixture
def lorem_post():
    post = BlogPost.objects.create(
        author=mixer.blend(get_user_model()),
        title="Lorem ipsum is awesome!",
        subtitle="The best nonsense",
        content="""Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim, quod, eum fuga obcaecati 
        eligendi doloremque sed ea dicta harum accusantium et, voluptas sint facere rem. Tempora pariatur commodi cum nobis.""",
    )
    return post


@pytest.fixture
def blog_content_random():
    """ Creates 5 Posts with random authors and 1 to 5 labels"""

    mixer.cycle(5).blend(get_user_model())
    for i in range(5):
        post = mixer.blend('blog.BlogPost', author=mixer.SELECT)
        add_new_label = 1
        try:
            post.tags.add("hello", "world", "its", "beautiful")
        except:
            pass
