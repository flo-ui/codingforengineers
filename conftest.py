import pytest
import random
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from blog.models import BlogPost, BlogPostLabel

@pytest.fixture
def lorem_post():
    post = mixer.blend(
        'blog.BlogPost',
        author=mixer.blend(User),
        content="""Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim, quod, eum fuga obcaecati 
        eligendi doloremque sed ea dicta harum accusantium et, voluptas sint facere rem. Tempora pariatur commodi cum nobis."""
    )
    return post


@pytest.fixture
def blog_content_random():
    for i in range(5):
        label = mixer.blend('blog.BlogPostLabel')
        mixer.blend(User)
        post = mixer.blend('blog.BlogPost', author=mixer.SELECT)
        post.labels.add(label)