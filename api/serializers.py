from rest_framework import serializers
from .models import Group, Product, Lesson, UserProductAccess


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'start_datetime', 'cost', 'lessons_count']

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(product=obj).count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class UserProductAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProductAccess
        fields = ['user', 'product']
