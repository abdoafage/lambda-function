import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_GetAllFunctions(AdminUser, load_functions_to_database, api_client):
    client = api_client(AdminUser)

    load_functions_to_database()

    url = reverse("GetAllFunctions")

    print(url)

    res = client.get(url)

    print(len(res.json()))

    assert res.status_code == 200

    assert len(res.json()) == 4
