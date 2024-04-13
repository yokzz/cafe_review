from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=63)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    pub_date = models.DateTimeField(auto_now_add=True)