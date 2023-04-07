from django.urls import path
from .views import UserView, PostView, CreatePostView, EditPostView


urlpatterns = [
    path('users', UserView.as_view()),
    path('posts', PostView.as_view()),
    path('create', CreatePostView.as_view()),
    path('edit', EditPostView.as_view())
]
