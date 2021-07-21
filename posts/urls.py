from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostsViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostsViewSet, basename='posts')

urlpatterns = router.urls