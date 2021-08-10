from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

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

    def create(self, request, *args, **kwargs):
        """Creates a new user and returns a token for authentication"""
        data = request.data
        response = {
            "status": False,
            "message": "",
            "data": {}
        }

        users = User.objects.filter(username=data["username"])
        if users.exists():
            response["message"] = "Bu telefon raqam orqali avval ro'yhatdan o'tilgan!"
            return Response(response, status=201)

        user = User.objects.create_user(username=data["username"], password=data["password"])
        token, created = Token.objects.get_or_create(user=user)

        response["status"] = True
        response["message"] = "Tabriklaymiz! Siz muvaffaqiyatli tarzda ro'yhatdan o'tdingiz!"
        response["data"]["username"] = data["username"]
        response["data"]["token"] = token.key

        return Response(response, status=201)


class CategoryViewSet(ModelViewSet):
    """
    View to list categories
    """
    permission_classes = (SuperUserOnly, IsAuthenticatedOrReadOnly)
    authentication_classes = [TokenAuthentication]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


    @action(detail=False, methods=["get"])
    def audiobooks(self, request):
        categories = Category.objects.filter(category_type="audiobooks")
        
        page = self.paginate_queryset(categories)

        if page is not None:
            serializer = CategorySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serialized_categories = CategorySerializer(categories, many=True)
        return Response(data=serialized_categories.data)
    

    @action(detail=False, methods=["get"])
    def readables(self, request):
        categories = Category.objects.filter(category_type="readables")

        page = self.paginate_queryset(categories)

        if page is not None:
            serializer = CategorySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serialized_categories = CategorySerializer(categories, many=True)
        return Response(data=serialized_categories.data)


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