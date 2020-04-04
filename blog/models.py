from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

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


class PostFile(models.Model):
    expiration_choices = [
        ('1','One Day'),
        ('7','One Week'),
        ('30','One Month'),
        ('365','One Year')
    ]
    title = models.CharField(max_length=100)
    expiration = models.CharField(max_length=20,choices=expiration_choices, default=1)
    content = models.TextField()
    file = models.FileField(upload_to = 'files/', blank = True , null = True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  reverse('postfile-detail', kwargs={'pk': self.pk})
    
    def snippet(self):
        str = self.content[:100]
        if len(self.content) > 100:
            str+='...'
        return str

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.file.delete()

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


class Attachment(models.Model):
    post = models.ForeignKey(PostFile, on_delete = models.CASCADE)
    file = models.FileField(upload_to='files/', blank = True, null= True)

    def filename(self):
        return os.path.basename(self.file.name)
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
