from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.throttling import UserRateThrottle


from .models import Function
from .serializers import FunctionSerializer, UpdateFunctionSerializer
from .utility import execute_python_code
from .permissions import IsOwnerOfFunction

# Create your views here.


class CreateFunction(CreateAPIView):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        serializer.save(owner=self.request.user)
        print(self.request.user)


class UpdateFunction(UpdateAPIView):
    permission_classes = [IsOwnerOfFunction, IsAuthenticated]
    queryset = Function.objects.all()
    serializer_class = UpdateFunctionSerializer
    lookup_field = "id"


class DeleteFunction(DestroyAPIView):
    permission_classes = [IsOwnerOfFunction, IsAuthenticated]
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer
    lookup_field = "id"


class GetFunction(RetrieveAPIView):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer
    lookup_field = "id"


class RunFunction(APIView):
    permission_classes = [IsOwnerOfFunction, IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    throttle_classes = [UserRateThrottle]

    def get_object(self):
        try:
            function = Function.objects.get(id=self.kwargs["id"])
            self.check_object_permissions(self.request, function)
            return function

        except Function.DoesNotExist:
            raise NotFound("Object not found")

    def post(self, request, id):
        func = self.get_object()

        func.increase_n_of_call()

        code = func.body
        params = request.data

        ret = execute_python_code(code, func.name, params)

        return Response(ret, status=status.HTTP_200_OK)


class TestFunction(APIView):
    permission_classes = [IsOwnerOfFunction, IsAuthenticated]

    def get_object(self):
        try:
            function = Function.objects.get(id=self.kwargs["id"])
            self.check_object_permissions(self.request, function)
            return function

        except Function.DoesNotExist:
            raise NotFound("Object not found")

    def post(self, request, id):
        func = self.get_object()

        code = func.body
        params = request.data

        ret = execute_python_code(code, func.name, params)

        return Response(ret, status=status.HTTP_200_OK)


class GetAllFunctions(ListAPIView):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer
