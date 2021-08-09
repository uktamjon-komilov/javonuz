from django.db import models


class Category(models.Model):
    CATEGORY_TYPES = [
        ("BOOKS", "BOOKS"),
        ("AUDIOBOOKS", "AUDIOBOOKS"),
        ("BOTH", "BOTH")
    ]
    
    name = models.CharField(max_length=255)
    category_type = models.CharField(choices=CATEGORY_TYPES, max_length=255)

    def __str__(self):
        return self.name