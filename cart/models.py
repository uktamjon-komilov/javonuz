from django.db import models

from account.models import User
from library.models import Book, AudioBook, PaperBack


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class CartItemBook(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cart) + str(self.book)


class CartItemAudioBook(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    audio_book = models.ForeignKey(AudioBook, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cart) + str(self.audio_book)


class CartItemPaperBack(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    paper_back = models.ForeignKey(PaperBack, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cart) + str(self.paper_back)