from django.conf import settings
from django.db import models
from listings.models import Listing

# Create your models here.
class ExchangeRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Oczekujące'),
        ('accepted', 'Zaakceptowane'),
        ('rejected', 'Odrzucone'),
        ('cancelled', 'Anulowane'),
    ]

    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='exchange_requests'
    )

    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='exchange_requests'
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request #{self.id} for Listing #{self.listing.id}"
