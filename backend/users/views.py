from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import status
from rest_framework.exceptions import ValidationError


from .serializers import UserSerializer

# Create your views here.
User = get_user_model()


class RegisterUser(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if User.objects.filter(username=username).exists():
            print("found it")
            return Response(
                {"error": "Username is already taken"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create a new user
        User.objects.create_user(username=username, password=password, email=email)

        return Response(
            {"message": "Registration successful"}, status=status.HTTP_201_CREATED
        )


class LoginUser(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            # print(token, _)
            return Response({"token": str(token), "_": _})
        else:
            # Handle invalid credentials
            return Response({"error": "Invalid credentials"}, status=400)


class LogoutUser(APIView):
    permission_classes = [
        IsAuthenticated,
    ]  # Ensure only authenticated users can access this view
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def post(self, request):
        # print(request)
        # authorization_header = request.META.get("HTTP_AUTHORIZATION")
        # print(authorization_header)
        print(request.user.auth_token)
        request.user.auth_token.delete()
        logout(request)
        return Response({"message": "Successfully logged out"})


class GetAllUsers(APIView):
    def get(self, request):
        users = User.objects.prefetch_related("function_set").all()

        serializers = UserSerializer(users, many=True).data

        return Response(serializers)


class GetUser(APIView):
    def get(self, request, id):
        user = User.objects.get(id=id)

        serializers = UserSerializer(user, many=False).data

        return Response(serializers)


# {"username":"abdoYasser2020","password":"183461"}
