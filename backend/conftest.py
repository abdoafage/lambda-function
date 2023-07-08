import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.core.management import call_command


User = get_user_model()


@pytest.fixture(scope="module")
def api_client():
    def wrapper(user=None):
        client = APIClient()
        if not isinstance(user, User):
            user = User.objects.create_user(
                username="admin",
                email="admin@gmail.com",
                password="adminadmin",
                is_staff=True,
                is_superuser=True,
                is_active=True,
            )
        client.force_authenticate(user=user)
        return client

    return wrapper


@pytest.fixture(scope="session")
def load_functions_to_database(django_db_setup, django_db_blocker):
    """
    load_functions_to_database() used to load all functions
    from lambda_functions.json to database.
    """

    def func():
        with django_db_blocker.unblock():
            call_command("load_functions", "lambda_functions.json")

    return func


@pytest.fixture
def create_user_obj(db):
    """
    create_app_user() used to create any type of user normal/admin
    (normal user by default).
    """

    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = "first",
        last_name: str = "last",
        email: str = "user@gmail.com",
        is_staff: bool = False,
        is_superuser: bool = False,
        is_active: bool = False,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user

    return create_app_user


@pytest.fixture
def AdminUser(db, create_user_obj):
    """
    create only admin user.
    """
    return create_user_obj(
        username="admin",
        password="adminadmin",
        is_staff=True,
        is_superuser=True,
        is_active=True,
    )
