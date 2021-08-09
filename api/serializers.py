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