from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ProductViewSet, LessonViewSet,
                    GroupViewSet, UserProductAccessViewSet)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'access', UserProductAccessViewSet, basename='access')

urlpatterns = [
    path('', include(router.urls)),
]
