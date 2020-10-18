from django.urls import path

from . import views
from .views import PostDetailView, PostListView

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
]
