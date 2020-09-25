import pytest
from random import randint
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
    """ Creates 5 Posts with random authors and 1 to 5 labels"""

    mixer.cycle(5).blend(User)
    labels = mixer.cycle(5).blend('blog.BlogPostLabel')
    for i in range(5):
        post = mixer.blend('blog.BlogPost', author=mixer.SELECT)
        add_new_label = 1
        while add_new_label > 0:
            try:
                post.labels.add(labels[randint(0, 4)])
            except:
                pass
            add_new_label = randint(0, 2)  # 1/3 chance to stop adding
