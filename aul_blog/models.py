from django.db import models
from django.utils import timezone
# Create your models here.



class blog_post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', default='default/default.jpg')
    tags = models.TextField(max_length=500)
    category = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    # category = models.
    

    def __str__(self):
        return self.title

