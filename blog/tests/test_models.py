import pytest
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from blog.models import BlogPost, BlogPostLabel

@pytest.mark.django_db
class TestBlogPostLabel:

    def test_blog_post_label_creation(self):
        label = mixer.blend('blog.BlogPostLabel')
        assert label.pk == 1, 'Create Label instance'


@pytest.mark.django_db
class TestBlogPost:
    def test_blog_post_creation(self,lorem_post):
        assert lorem_post.pk == 1, 'Create Post instance'

    def test_post_snippet_end(self,lorem_post):
        snippet = lorem_post.snippet(8)
        assert snippet == "Lorem ip", 'posts snippet method only end arg' 

    def test_post_snippet_start_end(self, lorem_post):
        snippet = lorem_post.snippet(8, 2)
        assert snippet == "rem ip", 'post snippet method end- and start arg'

    def test_post_str(self, lorem_post):
        assert str(lorem_post) == lorem_post.title

    def test_label_str(self):
        label = mixer.blend('blog.BlogPostLabel')
        assert str(label) == label.name


@pytest.mark.django_db
class TestBlogLabeling:
    def test_blog_content(self, blog_content_random): #test fixture
        assert BlogPost.objects.all().count() == 5, 'validating number of generated blogposts'
        assert BlogPost.objects.get(pk=2).labels.all().count() in range(1,5), 'validating the addition of labels'

