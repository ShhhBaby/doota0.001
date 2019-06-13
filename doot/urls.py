from rest_framework import routers
from .api import postViewSet


router = routers.DefaultRouter()
router.register('api/posts', postViewSet, 'api')

urlpatterns =router.urls