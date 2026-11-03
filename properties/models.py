from django.db import models
from django.conf import settings


class Property(models.Model):

    PROPERTY_TYPES = (
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
        ('land', 'Land'),
        ('commercial', 'Commercial'),
    )

    STATUS_CHOICES = (
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    price = models.PositiveBigIntegerField()
    area = models.PositiveIntegerField()
    rooms = models.PositiveSmallIntegerField()

    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='properties'
    )

    amenities = models.ManyToManyField(
    'Amenity',
    blank=True,
    related_name='properties'
)

created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title

class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

amenities = models.ManyToManyField(
    'Amenity',
    blank=True,
    related_name='properties'
)

class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(upload_to='properties/')

    def __str__(self):
        return f"Image for {self.property.title}"