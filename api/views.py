from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import BookSerializer, CategorySerializer, UserSerializer
from .permissions import UpdateOwnUserProfile, SuperUserOnly

from account.models import User
from category.models import Category
from library.models import Book


class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserViewSet(ModelViewSet):
    """
    View to create, update, delete users in the system.
    """
    permission_classes = (UpdateOwnUserProfile,)
    authentication_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CategoryViewSet(ModelViewSet):
    """
    View to list categories
    """
    permission_classes = (SuperUserOnly, IsAuthenticatedOrReadOnly)
    authentication_classes = [TokenAuthentication]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BookViewSet(ModelViewSet):
    """
    View to list books
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = [TokenAuthentication]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


    def get_queryset(self):
        params = self.request.query_params

        if "category_id" in params:
            category_id = params["category_id"]
            return self.queryset.filter(category__id=category_id)

        return self.queryset