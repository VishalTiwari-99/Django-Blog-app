from django.urls import path
from .views import (AboutView, PostListView, PostDetailView, CreatePostView, UpdatePostView,
                PostDeleteView, DraftListView, add_comment_to_post, comment_approve, comment_remove,
                post_publish)

urlpatterns = [
    path('',PostListView.as_view(),name='post_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/<pk>/', PostDetailView.as_view(),name='post_detail'),
    path('post/', CreatePostView.as_view(),name="post_new"),
    path('post/<pk>/edit/', UpdatePostView.as_view(), name='post_edit'),
    path('post/<pk>/remove/', PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', DraftListView.as_view(), name='post_draft_list'),
    path('post/<pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<pk>/approve/', comment_approve, name="comment_approve"),
    path('comment/<pk>/remove/', comment_remove, name='comment_remove'),
    path('post/<pk>/publish/', post_publish, name='post_publish')
]
