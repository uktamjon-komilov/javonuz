from django.db.models import base
from django.urls import path, include
from django.utils.translation import deactivate

from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import *


router = DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("categories", CategoryViewSet, basename="category")
router.register("books", BookViewSet, basename="book")


urlpatterns = [
    path("login/", UserLoginApiView.as_view()),
    path("", include(router.urls)),
]