from rest_framework import serializers
from .models import Function


class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = "__all__"
        # depth = 1


class UpdateFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        # fields = "__all__"
        exclude = ["owner"]
