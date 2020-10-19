from os import name

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

import pytest
from mixer.backend.django import mixer

from blog.models import BlogPost
from conftest import lorem_post


@pytest.mark.django_db
class TestBlogPost:
    def test_blog_post_creation(self, lorem_post):
        assert lorem_post.pk == 1, 'Create Post instance'
        assert str(lorem_post) == lorem_post.title
        assert lorem_post.slug == "lorem-ipsum-is-awesome"

    def test_blog_post_file_upload_invalid(self, lorem_post):
        """ run file validator with a filetype other than .md"""

        mock_file = SimpleUploadedFile("will_fail.rmd", b"some text")
        lorem_post.file = mock_file
        with pytest.raises(ValidationError):
            lorem_post.full_clean()  # calls all validators

    def test_blog_post_file_upload_valid(self, lorem_post):
        mock_file = SimpleUploadedFile("will_pass.md", b"# some important test")
        lorem_post.file = mock_file
        lorem_post.full_clean()
        assert lorem_post.file.name == "will_pass.md"

    def test_post_snippet_end(self, lorem_post):
        snippet = lorem_post.snippet(8)
        assert snippet == "Lorem ip", 'posts snippet method only end arg'

    def test_post_snippet_start_end(self, lorem_post):
        snippet = lorem_post.snippet(8, 2)
        assert snippet == "rem ip", 'post snippet method end- and start arg'

    def test_label_str(self, lorem_post):
        lorem_post.tags.add("lorem", "ipsum")
        assert "lorem" in lorem_post.tags.slugs()


@pytest.mark.django_db
class TestBlogLabeling:
    def test_blog_content(self, blog_content_random):  # test fixture
        assert (
            BlogPost.objects.all().count() == 5
        ), 'validating number of generated blogposts'
