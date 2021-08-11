from cart.models import Cart
from library.models import AudioBook, AudioFile, Book, PaperBack
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from account.models import User
from category.models import Category


class UserSerializer(ModelSerializer):
    """Serializes a user object"""

    class Meta:
        model = User
        fields = ["id", "fullname", "username", "password", "balance"]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password"
                }
            },
            "balance": {
                "read_only": True,
            }
        }
    

    def create(self, validated_data):
        """Create and return a new user account"""
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )

        return user
    

    def update(self, instance, validated_data):
        """Update and return a user's account"""

        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)
        
        return super().update(instance, validated_data)



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "category_type"]



class PaperBackSerializer(ModelSerializer):
    class Meta:
        model = PaperBack
        fields = ["price", "stock", "thumbnail"]


class AudioFileSerializer(ModelSerializer):
    class Meta:
        model = AudioFile
        fields = ["chapter", "file"]


class AudioBookSerializer(ModelSerializer):
    files = AudioFileSerializer(source="audio_file", many=True, read_only=True)

    class Meta:
        model = AudioBook
        fields = ["price", "stock", "thumbnail", "files"]


class CategorySerializer(ModelSerializer):
    content_count = SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "category_type", "content_count"]
    
    def get_content_count(self, obj):
        return Book.objects.filter(category=obj).count()


class BookSerializer(ModelSerializer):
    paper_back = PaperBackSerializer(read_only=True)
    audio_book = AudioBookSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "thumbnail", "author", "category", "pages", "chapter", "description", "price", "stock", "content_file", "paper_back", "audio_book"]


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = []