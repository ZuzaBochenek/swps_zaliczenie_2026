from django.db import models

# Create your models here.
class Material(models.Model):
    TYPE_CHOICES = [
        ('book', 'Książka'),
        ('notes', 'Notatki'),
    ]

    SUBJECT_CHOICES = [
        ('social', 'Psychologia społeczna'),
        ('cognitive', 'Psychologia poznawcza'),
        ('general', 'Psychologia ogólna'),
        ('developmental', 'Psychologia rozwojowa'),
        ('neuro', 'Neuropsychologia'),
    ]
    class Material(models.Model):
    # choices
    TYPE_CHOICES = [
        ('book', 'Książka'),
        ('notes', 'Notatki'),
    ]

    SUBJECT_CHOICES = [
        ('social', 'Psychologia społeczna'),
        ('cognitive', 'Psychologia poznawcza'),
        ('general', 'Psychologia ogólna'),
        ('developmental', 'Psychologia rozwojowa'),
        ('neuro', 'Neuropsychologia'),
    ]
    # pola modelu
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)

    material_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
    )

    condition = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    study_year = models.PositiveSmallIntegerField(
        choices=[(i, f'{i}') for i in range(1, 6)]
    )

    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    # metody pomocnicze
    def __str__(self):
        return f"{self.title} ({self.get_material_type_display()})"