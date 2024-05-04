from django.db import models
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class Puzzle(models.Model):
    word = models.CharField(max_length=5)

class Tentativa(models.Model):
    puzzle = models.ForeignKey(Puzzle,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tentativa = models.IntegerField(default=0)

class Comment(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    puzzle_id = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)