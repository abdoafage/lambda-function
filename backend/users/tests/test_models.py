import pytest
from faker import Faker
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.users
@pytest.mark.models
@pytest.mark.django_db
def test_users():
    fake = Faker()
    username = fake.name()
    email = fake.email()
    password = fake.password()

    User.objects.create_user(username=username, email=email, password=password)
    user = User.objects.get(username=username)

    assert user.username == username
    assert user.check_password(password) is True
    assert user.email == email
    assert User.objects.count() == 1
