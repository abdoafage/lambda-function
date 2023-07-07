from rest_framework import serializers
from django.contrib.auth import get_user_model
from functions.serializers import FunctionSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    function_set = FunctionSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"  # ["username", "password", "email", "function_set"]
