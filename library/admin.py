from django.contrib import admin
from library.models import AudioBook, Book, PaperBack, AudioFile


class AudioFileStackedInlineAdmin(admin.StackedInline):
    model = AudioFile
    fields = ["chapter", "file"]


class AudioBookAdmin(admin.ModelAdmin):
    inlines = [AudioFileStackedInlineAdmin]


admin.site.register(Book)
admin.site.register(PaperBack)
admin.site.register(AudioBook, AudioBookAdmin)