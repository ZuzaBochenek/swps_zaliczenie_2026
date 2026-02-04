from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
class Review(models.Model):
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='given_reviews'
    )

    reviewed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_reviews'
    )

    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )

    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Review {self.rating}/5 by {self.reviewer}"