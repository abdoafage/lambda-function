# import pytest
# from django.contrib.auth import get_user_model
# from rest_framework.test import APIClient


# User = get_user_model()


# @pytest.fixture(scope="module")
# # @pytest.mark.django_db
# def  api_client():
#     def wrapper(user=None):
#         client = APIClient()
#         if not isinstance(user, User):
#             user = User.objects.create_user(
#                 username="test", email="a@test.com", password="secret123")
#         client.force_authenticate(user = user)
#         return client
#     return wrapper
