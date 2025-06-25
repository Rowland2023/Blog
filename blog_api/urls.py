from django.urls import path
from rest_framework.routers import DefaultRouter
from.views import PostViewSet ,CommentViewSet,register,login,profile,post_comments

router = DefaultRouter()
router.register(r'posts',PostViewSet)
router.register(r'comments',CommentViewSet)

urlpatterns =[
    path('register/' ,register),
    path('login/',login) , 
    path('profile/',profile),
    path('posts/<int:post_id>/comments/', post_comments, name='post-comments'),
]

urlpatterns += router.urls