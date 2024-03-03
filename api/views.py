from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Group, Product, Lesson, UserProductAccess
from .serializers import (GroupSerializer, ProductListSerializer,
                          LessonSerializer, UserProductAccessSerializer)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.filter(start_datetime__lte=timezone.now())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        lesson_id = kwargs.get('pk')

        if not user.is_authenticated:
            return Response({"detail": "Пользователь не авторизован. "
                             "Авторизуйтесь, чтобы получить доступ."},
                            status=401)

        lesson = get_object_or_404(Lesson, pk=lesson_id)

        try:
            UserProductAccess.objects.get(user=user, product=lesson.product)
        except UserProductAccess.DoesNotExist:
            raise PermissionDenied(detail="У вас нет доступа к этому уроку.")

        serializer = LessonSerializer(lesson)
        return Response(serializer.data)


class UserProductAccessViewSet(viewsets.ModelViewSet):
    queryset = UserProductAccess.objects.all()
    serializer_class = UserProductAccessSerializer

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)

        user_product_access = serializer.save()
        user = user_product_access.user
        product_id = user_product_access.product.id

        groups = Group.objects.filter(product_id=product_id)

        groups = groups.annotate(num_users=Count('users'))

        sorted_groups = sorted(groups, key=lambda x: x.num_users)
        selected_group = sorted_groups[0]

        selected_group.users.add(user)
        selected_group.current_members_count = selected_group.users.count()
        selected_group.save()
        return serializer.save()
