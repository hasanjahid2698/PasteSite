from django.urls import path
from .views import (
    PostListView,
    MyPostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostFileCreateView,
    PostFileListView,
    PostFileDetailView,
    PostFileUpdateView,
    PostFileDeleteView,
    PostFileUpdate,
    PostFileShare,
)
from . import views

urlpatterns = [
    # path('', PostListView.as_view(), name='blog-Home'),
    path('', PostFileListView.as_view(), name='blog-Home'),

    path('/mypaste/', MyPostListView.as_view(), name='blog-myHome'),

    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/', PostFileDetailView.as_view(), name='postfile-detail'),

    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:id>/update/', PostFileUpdate, name='post-update'),

    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/delete/', PostFileDeleteView.as_view(), name='post-delete'),

    path('post/<int:id>/share/', PostFileShare, name='post-share'),

    # path('post/text/new/', PostCreateView.as_view(), name='posttext-create'),
    path('post/file/new/', PostFileCreateView.as_view() , name='postfile-create'),
]
