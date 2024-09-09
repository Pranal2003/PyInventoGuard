from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
Category = (
    ('Super','Super'),
    ('Hyper','Hyper'),
    ('Sport','Sport'),
)
Color = (
    ('-','-'),
    ('red','red'),
    ('yellow','yellow'),
    ('blue','blue'),
)
class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=50,choices=Category,null=True)
    quantity = models.PositiveIntegerField(null=True)
    color = models.CharField(max_length=50,choices=Color,null=True)
    image = models.ImageField(default='Car.jpg',upload_to='cars_images')
    def __str__(self):
        return f'{self.name}'
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    color = models.CharField(max_length=50,choices=Color,null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        # Set the time zone to Indian Standard Time (IST)
        timezone.activate('Asia/Kolkata')
        super(Order, self).save(*args, **kwargs)
    def __str__(self):
        return f'{self.product} order by {self.staff.username}'
