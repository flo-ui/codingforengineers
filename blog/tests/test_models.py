import pdb
import shutil
from os import name

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings

import pytest

from blog.models import BlogPost
from conftest import lorem_post

from .factories import BlogPostFactory, BlogPostFileFactory, SuperUserFactory

pytestmark = pytest.mark.django_db


TEST_DIR = "test_data"


class TestBlogPost:
    def test_post_creation(self, lorem_post):
        assert lorem_post.pk == 1, "Create Post instance"
        assert str(lorem_post) == "Lorem ipsum is awesome!"
        assert lorem_post.slug == "lorem-ipsum-is-awesome"

    def test_post_slug(self):
        post = BlogPostFactory(title="Harry Potter")
        assert post.slug == "harry-potter"
        post.title = "Hermione Granger"
        post.save()
        assert post.slug == "harry-potter"

    def test_post_invalid_no_data(self):
        """ No data is passed into the model-admin """
        with pytest.raises(ValidationError):
            post = BlogPost.objects.create(
                author = SuperUserFactory()
            )
            post.full_clean()
            
    def test_post_file_upload_invalid_file(self, lorem_post):
        """ run file validator with a filetype other than .md"""

        file = SimpleUploadedFile("will_fail.rmd", b"# some text\n\n wow")
        lorem_post.file = file
        with pytest.raises(ValidationError):
            lorem_post.full_clean()  # calls all validators
            lorem_post.save()

    def test_blog_post_file_upload_valid(self, lorem_post):
        """ run file validator with a .md-file"""
        file = SimpleUploadedFile("will_pass.md", b"# some very good heading\n\n * List item")
        lorem_post.file = file
        lorem_post.full_clean()
        assert lorem_post.file.name == "will_pass.md"

    def test_post_snippet_end(self, lorem_post):
        snippet = lorem_post.snippet(8)
        assert snippet == "Lorem ip", "posts snippet method only end arg"

    def test_post_snippet_start_end(self, lorem_post):
        snippet = lorem_post.snippet(8, 2)
        assert snippet == "rem ip", "post snippet method end- and start arg"

    def test_post_tags(self, lorem_post):
        lorem_post.tags.add("lorem", "ipsum")
        assert "lorem" in lorem_post.tags.slugs()

    @override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
    def test_post_save(self):
        file = SimpleUploadedFile('content.md', b"# Test 1\n\n* list item 1")
        post = BlogPost.objects.create(
            author=get_user_model().objects.create(
                username="petermueller", password="ilmerkel"
            ),
            file=file,
        )
        assert post.file.name == "uploads/content.md"
        assert post.title == "Test 1"
        assert post.content == "* list item 1"

        try:
            shutil.rmtree(TEST_DIR)
        except OSError:
            pass


class TestBlogLabeling:
    def test_blog_content(self):  # test fixture
        BlogPostFactory()
        assert BlogPost.objects.count() == 1, "validating number of generated blogposts"
