from rest_framework import viewsets
from . models import Post ,Comment
from .serializers import PostSerializer ,CommentSerializer

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate

from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


# Create your views here.
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
class PostFilters(django_filters.FilterSet):
    created_at__gte = django_filters.DateFilter(field_name ='created_at' ,lookup_expr='gte')
    created_at__lte = django_filters.DateFilter(field_name = 'created_at' ,lookup_expr='lte')
    class Meta:
        model = Post
        fields = ['author' , 'created_at__gte', 'created_at__lte' ]
from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = PostFilters  # correct spelling for DRF!
    search_fields = ['title', 'content']

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']

    if User.objects.filter(username=username).exists():
        return Response({'error' :'User already exist'},status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username , email=email,password=password)
    token = Token.objects.create(user=user)
    return Response({'token' :token.key})

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username , password=password)

    if user is not None:
        token, _= Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
    return Response({'error':'Invalid credential'} , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])

def profile(request):
    user= request.user

    if request.method == 'GET':
        return Response({'username':user.username, 'email': user.email})
    
    elif request.method == 'PUT':
        user.email = request.data.get('email' , user.email)
        if 'password' in request.data:
            user.set_password(request.data['password'])
        user.save()
        return Response({'message' : 'Profile updated'})
    

from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_comments(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'GET':
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post, author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

