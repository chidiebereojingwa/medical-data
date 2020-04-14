from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
  name = models.CharField(max_length=200)
  illness = models.TextField()
  age = models.IntegerField(blank=True,null=True)
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  telephone = models.CharField(max_length=15,blank=True,null=True)
  def __str__(self):
    return self.name
  class Meta:
    verbose_name_plural = "Posts"