from django.urls import path
from . import views
from .views import (
    tags,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SearchQueryView,
)
from .feeds import LatestEntriesFeed

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('stream/', PostListView.as_view(), name='blog-stream'),
    path('islam/', views.islam, name='islam'),
    path('u/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/feed/', LatestEntriesFeed()),
    path('tag/<slug:tag_slug>', tags, name='tags'),
    path('search/', SearchQueryView.as_view(), name='search_query'),
    path('about/', views.about, name='blog-about'),
]
