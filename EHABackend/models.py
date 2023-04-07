from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import json


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to="media")
    categories = models.CharField(max_length=2000)
    date = models.DateField(auto_now_add=True)
    aprroved = models.BooleanField(default=False)

    def __str__(self):
        return f"Author: {self.author} | Title: {self.title} | Date: {self.date}"
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def set_categories(self, lst):
        self.categories = json.dumps(lst)

    def get_categories(self):
        return json.loads(self.categories)

