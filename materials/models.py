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