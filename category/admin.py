from django.contrib import admin
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(Category, CategoryAdmin)