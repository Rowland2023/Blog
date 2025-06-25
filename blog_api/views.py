from rest_framework import viewsets
from . models import Post ,Comment
from .serializers import PostSerializer ,CommentSerializer

# Create your views here.

class PostViewSets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
