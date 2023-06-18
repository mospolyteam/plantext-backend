from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, ReviewViewSet, UserViewSet, WriterViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'writers', WriterViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls