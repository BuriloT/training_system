from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    min_users = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_link = models.URLField()


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='group_users')
    current_members_count = models.IntegerField(default=0)

    def update_members_count(self):
        self.current_members_count = self.users.count()
        self.save()


class UserProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    access_datetime = models.DateTimeField(null=True, blank=True)
