from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import BlogPost


# Create your views here.
def index(request):
    index_posts = BlogPost.objects.all()[:5]
    context = {'index_posts': index_posts}
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


class PostListView(ListView):
    model = BlogPost
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    model = BlogPost
    context_object_name = 'post'
    template_name = 'blog/post.html'
