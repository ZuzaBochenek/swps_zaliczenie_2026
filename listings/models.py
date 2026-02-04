from django.db import models

# Create your models here.
class Listing(models.Model):
    MODE_CHOICES = [
        ('sale', 'Sprzedaż'),
        ('exchange', 'Wymiana'),
        ('both', 'Sprzedaż lub wymiana'),
    ]

    STATUS_CHOICES = [
        ('active', 'Aktywne'),
        ('reserved', 'Zarezerwowane'),
        ('closed', 'Zamknięte'),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='listings'
    )

    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='listings'
    )

    mode = models.CharField(
        max_length=10,
        choices=MODE_CHOICES,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
    )

    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
   def __str__(self):
        return f"Listing #{self.id} - {self.material.title}"