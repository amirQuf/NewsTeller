from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Category(models.Model):
    name = models.CharField(max_length = 30)
    slug  = models.SlugField(unique = True)
    is_active = models.BooleanField(default = True)
    position = models.IntegerField()
    class Meta:
        ordering= ['position']
    def __str__(self):
        return self.name


class News(models.Model):
    STATUS_CHOICE =(('P', 'Published'),
                    ('D','Draft'))
    title = models.CharField(max_length = 50)
    slug  = models.SlugField(unique = True)
    desc  = models.TextField()
    view  = models.PositiveIntegerField(default = 0 )
    created =models.DateTimeField(auto_now_add = True)
    publish = models.DateTimeField(default = timezone.now)
    update = models.DateTimeField(auto_now = True)
    cat  = models.ManyToManyField(Category)
    thumbnail  = models.ImageField(upload_to ='News')
    status  = models.CharField(max_length = 1,choices = STATUS_CHOICE)
    class Meta:
        ordering= ['view','-publish']
    def __str__(self):
        return self.title

class Favcategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    