from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Akeray(models.Model):

    RENTED = 'rented'
    AVAILABLE = 'available'

    STATUS_CHOICE = (
        (RENTED, 'Rented'),
        (AVAILABLE, 'Available')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True, blank=True)
    subcity = models.CharField(max_length=200, null=True, blank=True)
    kebele = models.CharField(max_length=20, null=True, blank=True)
    price = models.IntegerField()
    summary = models.TextField(blank=True , null=True)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default=AVAILABLE)

   
    def __str__(self):
        return '%s' % self.title 

    class Meta:
        verbose_name_plural = 'Akeray'
        ordering = ['-date_added']

User.akeray = property(lambda u:Akeray.objects.get_or_create(user=u)[0])
    
class AkerayImage(models.Model):
    akeray = models.ForeignKey(Akeray, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return '%s' % self.akeray.title

    class Meta:
        verbose_name_plural = 'Images'