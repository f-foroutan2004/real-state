from django.db import models
from django.conf import settings


class PropertyRequest(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='requests'
    )

    property = models.ForeignKey(
        'properties.Property',
        on_delete=models.CASCADE,
        related_name='requests'
    )

    visit_date = models.DateTimeField()

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.property.title}"