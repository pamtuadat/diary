from django.db import models
from django.conf import settings

# phan loai
class Category(models.Model):
    name = models.CharField(max_length=50)

# Nhãn
class Tag(models.Model):
    name = models.CharField(max_length=30)


class  Diary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    mood = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)


'''
Entity : Mood
'''
class Mood(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=10)
    color = models.CharField(max_length=20)

