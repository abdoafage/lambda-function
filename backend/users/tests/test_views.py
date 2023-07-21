import pytest
from faker import Faker
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.users
@pytest.mark.views
@pytest.mark.django_db
def test_RegisterUser():
    client = APIClient()
    fake = Faker()

    url = reverse("RegisterUser")

    data = {
        "username": fake.name().split(" ")[0],
        "email": fake.email(),
        "password": fake.password(),
    }
    response = client.post(url, data=data, format="json")

    res = response.json()
    assert response.status_code == 201
    assert res["message"] == "Registration successful"

    user = User.objects.get(username=data["username"])
    assert user.username == data["username"]
    assert user.check_password(data["password"]) is True
    assert user.email == data["email"]


@pytest.mark.users
@pytest.mark.views
@pytest.mark.django_db
def test_LoginUser():
    client = APIClient()
    fake = Faker()

    url = reverse("RegisterUser")

    data = {
        "username": fake.name().split(" ")[0],
        "email": fake.email(),
        "password": fake.password(),
    }
    client.post(url, data=data, format="json")

    url = reverse("LoginUser")

    response = client.post(
        url,
        data={"username": data["username"], "password": data["password"]},
        format="json",
    )

    res = response.json()

    assert response.status_code == 200
    assert res["_"] is True

    response = client.post(
        url,
        data={"username": data["username"], "password": data["password"]},
        format="json",
    )

    res = response.json()

    assert response.status_code == 200
    assert res["_"] is False


@pytest.mark.users
@pytest.mark.views
@pytest.mark.django_db
def test_LogoutUser():
    client = APIClient()
    fake = Faker()

    url = reverse("RegisterUser")

    data = {
        "username": fake.name().split(" ")[0],
        "email": fake.email(),
        "password": fake.password(),
    }
    client.post(url, data=data, format="json")

    url = reverse("LoginUser")

    response = client.post(
        url,
        data={"username": data["username"], "password": data["password"]},
        format="json",
    )

    res = response.json()

    assert response.status_code == 200
    assert res["_"] is True

    assert Token.objects.count() == 1

    # print(res)

    url = reverse("LogoutUser")
    client.credentials(HTTP_AUTHORIZATION="Token " + res["token"])
    response = client.post(url)
    # print(response.json())

    res = response.json()

    assert Token.objects.count() == 0
    assert res["message"] == "Successfully logged out"
