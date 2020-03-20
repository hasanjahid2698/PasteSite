from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class PostText(models.Model):
    expiration_choices = [
        ('1','One Day'),
        ('7','One Week'),
        ('30','One Month'),
        ('365','One Year')
    ]
    title = models.CharField(max_length=100)
    expiration = models.CharField(max_length=20,choices=expiration_choices, default=1)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  reverse('post-detail', kwargs={'pk': self.pk})