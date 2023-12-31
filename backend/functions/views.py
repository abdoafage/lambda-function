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
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    # def post(self, request, *args, **kwargs):
    #     return super().post(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        super().perform_create(serializer)
        serializer.save(owner=self.request.user)
        print(self.request.user)


class UpdateFunction(UpdateAPIView):
    permission_classes = [IsOwnerOfFunction, IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = Function.objects.all()
    serializer_class = UpdateFunctionSerializer
    lookup_field = "id"

    def patch(self, request, *args, **kwargs):
        print("request.data ", request.data)
        return super().patch(request, *args, **kwargs)


class DeleteFunction(DestroyAPIView):
    permission_classes = [IsOwnerOfFunction, IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer
    lookup_field = "id"


class GetFunction(RetrieveAPIView):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer
    permission_classes = [IsOwnerOfFunction, IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    lookup_field = "id"


class TestFunction(APIView):
    permission_classes = [IsOwnerOfFunction, IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_object(self):
        try:
            function = Function.objects.get(id=self.kwargs["id"])
            self.check_object_permissions(self.request, function)
            return function

        except Function.DoesNotExist:
            raise NotFound("Object not found")

    def post(self, request, id):
        func = self.get_object()

        self.increase_n_of_call(func)

        code = func.body
        params = request.data

        ret = execute_python_code(code, func.name, params)

        status_code = (
            status.HTTP_200_OK  # if ret["status"] == True else status.HTTP_400_BAD_REQUEST
        )

        return Response(ret, status=status_code)

    def increase_n_of_call(self, func):
        pass


class RunFunction(TestFunction):
    def increase_n_of_call(self, func):
        func.increase_n_of_call()


class GetAllFunctions(ListAPIView):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer
    permission_classes = [IsOwnerOfFunction, IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_queryset(self):
        queryset = Function.objects.filter(owner=self.request.user)
        return queryset
