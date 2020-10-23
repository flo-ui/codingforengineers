from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from django.core.mail import send_mail
from .models import BlogPost
from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def index(request):
    index_posts = BlogPost.objects.all()[:5]
    context = {'index_posts': index_posts}
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    print(settings.EMAIL_HOST_USER)
    if request.method == 'POST':
        #send_mail(
        #    request.POST["subject"], # Subject
        #    request.POST["sender_name"]+ ", "+ request.POST["sender_email"]+": \n\n"+ request.POST["message"], # Content
        #    settings.EMAIL_HOST_USER, # From
        #    [settings.EMAIL_RECIEVER], # To
        #    fail_silently=False,
        #)
        messages.success(request, 'Email was successfully sent')
        return redirect(reverse('blog:index'))
    return render(request, 'blog/contact.html')


class PostListView(ListView):
    model = BlogPost
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    model = BlogPost
    context_object_name = 'post'
    template_name = 'blog/post.html'
