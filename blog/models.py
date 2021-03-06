from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Skill(models.Model):
    text=models.TextField(default='')

class Education(models.Model):
    year1=models.IntegerField()
    year2=models.IntegerField()
    title=models.TextField(default='')
    details=models.TextField(default='')

class Work(models.Model):
    year1=models.IntegerField()
    year2=models.IntegerField()
    title=models.TextField(default='')
    details=models.TextField(default='')
    months=models.TextField(blank=True, null=True)
