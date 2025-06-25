from rest_framework.routers import DefaultRouter
from.views import PostViewSets ,CommentViewSets

router = DefaultRouter()
router.register(r'post',PostViewSets)
router.register(r'comments',CommentViewSets)

urlpatterns = router.urls