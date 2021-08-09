from rest_framework.fields import Field
from library.models import AudioBook, AudioFile, Book, PaperBack
from rest_framework.serializers import ModelSerializer

from account.models import User
from category.models import Category


class UserSerializer(ModelSerializer):
    """Serializes a user object"""

    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password"
                }
            }
        }
    

    def create(self, validated_data):
        """Create and return a new user"""
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )

        return user


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "category_type"]



class PaperBackSerializer(ModelSerializer):
    class Meta:
        model = PaperBack
        fields = ["price", "stock"]


class AudioFileSerializer(ModelSerializer):
    class Meta:
        model = AudioFile
        fields = ["chapter", "file"]


class AudioBookSerializer(ModelSerializer):
    files = AudioFileSerializer(source="audio_file", many=True, read_only=True)

    class Meta:
        model = AudioBook
        fields = ["price", "stock", "files"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class BookSerializer(ModelSerializer):
    paper_back = PaperBackSerializer(read_only=True)
    audio_book = AudioBookSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "author", "category", "pages", "chapter", "description", "price", "stock", "paper_back", "audio_book"]