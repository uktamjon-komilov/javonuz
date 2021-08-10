from library.utils import get_audio_path, get_book_path, get_thumbnail_path
from category.models import Category
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to=get_thumbnail_path, null=True)
    author = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()
    chapter = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0.0)
    stock = models.FloatField(default=0.0)

    content_file = models.FileField(upload_to=get_book_path, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PaperBack(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name="paper_back")
    thumbnail = models.ImageField(upload_to=get_thumbnail_path, null=True)
    price = models.FloatField(default=0.0)
    stock = models.FloatField(default=0.0)

    def __str__(self):
        return self.book.title


class AudioBook(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name="audio_book")
    thumbnail = models.ImageField(upload_to=get_thumbnail_path, null=True)
    price = models.FloatField(default=0.0)
    stock = models.FloatField(default=0.0)

    def __str__(self):
        return self.book.title


class AudioFile(models.Model):
    audio_book = models.ForeignKey(AudioBook, on_delete=models.CASCADE, related_name="audio_file")
    file = models.FileField(upload_to=get_audio_path)
    chapter = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.chapter}. {self.audio_book.book.title}"