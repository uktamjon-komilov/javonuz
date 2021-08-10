from django.db import models


class Category(models.Model):
    TYPES = [
        ("audiobooks", "audiobooks"),
        ("readables", "readables"),
    ]
    category_type = models.CharField(choices=TYPES, max_length=255, default="readables")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name