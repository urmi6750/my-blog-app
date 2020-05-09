from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('Post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('Post/new/', PostCreateView.as_view(), name='post-create'),
    path('Post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('Post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
