from category.models import Category
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet

from .serializers import CategorySerializer, UserSerializer
from .permissions import UpdateOwnUserProfile, SuperUserOnly

from account.models import User
from category.models import Category


class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserViewSet(ModelViewSet):
    """
    View to create, update, delete users in the system.
    """
    permission_classes = (UpdateOwnUserProfile,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CategoryViewSet(ModelViewSet):
    """
    View to list categories
    """
    permission_classes = (SuperUserOnly, )
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
