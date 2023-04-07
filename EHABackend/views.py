from rest_framework import generics, status
from .serializers import UserSerializer, PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


# All Users
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# All Posts
class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Create Post
class CreatePostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            author = serializer.data.get('author')
            title = serializer.data.get('title')
            description = serializer.data.get('description')
            image = serializer.data.get('image')
            categories = serializer.data.get('categories')
            date = serializer.data.get('date')
            approved = serializer.data.get('approved')

            newPost = Post(
                author=author,
                title=title,
                description=description,
                image=image,
                categories=categories,
                date=date,
                approved=approved
            )
            newPost.set_categories(categories)
            newPost.save()

        return Response(PostSerializer(newPost).data, status=status.HTTP_201_CREATED)
    

# Edit Post
class EditPostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            author = serializer.data.get('author')
            title = serializer.data.get('title')
            description = serializer.data.get('description')
            image = serializer.data.get('image')
            categories = serializer.data.get('categories')
            date = serializer.data.get('date')
            approved = serializer.data.get('approved')

            newPost = Post(
                author=author,
                title=title,
                description=description,
                image=image,
                categories=categories,
                date=date,
                approved=approved
            )
            newPost.set_categories(categories)
            newPost.save()

        return Response(PostSerializer(newPost).data, status=status.HTTP_201_CREATED)

