import pytest
from faker import Faker
from users.serializers import CreateUserSerializer, UserSerializer
from functions.models import Function
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.users
@pytest.mark.serializers
@pytest.mark.django_db
def test_CreateUserSerializer():
    fake = Faker()

    username = fake.name().split(" ")[0]
    email = fake.email()
    password = fake.password()

    user = CreateUserSerializer(
        data={"username": username, "email": email, "password": password}
    )

    user.is_valid(raise_exception=True)
    user.save()

    assert User.objects.count() == 1

    user_ = User.objects.get(username=username)
    assert user_.username == username
    assert user_.check_password(password) is True
    assert user_.email == email


@pytest.mark.django_db
def test_UserSerializer():
    fake = Faker()

    username = fake.name().split(" ")[0]
    email = fake.email()
    password = fake.password()

    user = CreateUserSerializer(
        data={"username": username, "email": email, "password": password}
    )

    user.is_valid(raise_exception=True)
    user.save()

    user_ = User.objects.get(username=username)

    func1 = Function.objects.create(
        name="find_max",
        body="def find_max(nums):\n    return max(nums)",
        owner=user_,
    )

    print(func1)

    serializer = UserSerializer(user_).data

    print(serializer["function_set"][0]["name"])
    assert serializer["function_set"][0]["name"] == "find_max"
    assert (
        serializer["function_set"][0]["body"]
        == "def find_max(nums):\n    return max(nums)"
    )
    assert serializer["function_set"][0]["owner"] == user_.id

    assert serializer["username"] == username
    assert serializer["username"] == user_.username
