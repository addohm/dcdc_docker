from django.db import models
from django.utils.timezone import now


class Staff(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='staff/')
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CarouselImage(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='carousel/')

    def __str__(self):
        return self.description or f"Image {self.id}"

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.CharField(max_length=8)

    def __str__(self):
        return self.title
    
class DiveSite(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    country = models.CharField(max_length=255)
    citystateprov = models.CharField(max_length=255, verbose_name='City\\State\\Province')
    map_url = models.URLField(max_length=255)
    image = models.ImageField(upload_to='sites/')

    def __str__(self):
        return self.name

class Social(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=255)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    email = models.EmailField(verbose_name='E-Mail')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    subject = models.CharField(max_length=255, verbose_name='Subject')
    message =models.TextField(verbose_name='Message')
    when_sent = models.DateTimeField(default=now, editable=False)
    replied = models.BooleanField(default=False)
    when_replied = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
