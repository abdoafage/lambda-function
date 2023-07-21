import pytest
from django.urls import reverse
from functions.models import Function


@pytest.mark.functions
@pytest.mark.views
@pytest.mark.django_db
def test_GetAllFunctions(AdminUser, load_functions_to_database, api_client):
    client = api_client(AdminUser)

    load_functions_to_database()

    url = reverse("GetAllFunctions")

    res = client.get(url)

    assert res.status_code == 200

    assert len(res.json()) == 4


@pytest.mark.functions
@pytest.mark.views
@pytest.mark.django_db
def test_RunFunction(AdminUser, load_functions_to_database, api_client):
    client = api_client(AdminUser)

    load_functions_to_database()

    functions = Function.objects.all()

    # first run for first function.
    first_function = functions[0]

    url = f"http://localhost:8000/functions/run/{first_function.id}/"

    a, b = 3, 6

    response = client.post(url, {"a": a, "b": b}, format="json")

    res = response.json()

    assert res["status"] is True

    assert Function.objects.get(id=first_function.id).numberOfCalls == 1

    assert Function.objects.get(id=first_function.id).owner == AdminUser

    assert res["message"] == a + b

    # second run for first function.
    response = client.post(url)

    res = response.json()

    assert response.status_code == 400

    assert res["status"] is False

    assert Function.objects.get(id=first_function.id).numberOfCalls == 2

    assert Function.objects.get(id=first_function.id).owner == AdminUser

    assert (
        res["message"]
        == "add_numbers() missing 2 required positional arguments: 'a' and 'b'"
    )


@pytest.mark.functions
@pytest.mark.views
@pytest.mark.django_db
def test_TestFunction(AdminUser, load_functions_to_database, api_client):
    client = api_client(AdminUser)

    load_functions_to_database()

    functions = Function.objects.all()

    # first run for first function.
    first_function = functions[0]

    url = f"http://localhost:8000/functions/test/{first_function.id}/"

    a, b = 3, 6

    response = client.post(url, {"a": a, "b": b}, format="json")

    res = response.json()

    assert res["status"] is True

    assert Function.objects.get(id=first_function.id).numberOfCalls == 0

    assert Function.objects.get(id=first_function.id).owner == AdminUser

    assert res["message"] == a + b

    # second run for first function.
    response = client.post(url)

    res = response.json()

    assert response.status_code == 400

    assert res["status"] is False

    assert Function.objects.get(id=first_function.id).numberOfCalls == 0

    assert Function.objects.get(id=first_function.id).owner == AdminUser

    assert (
        res["message"]
        == "add_numbers() missing 2 required positional arguments: 'a' and 'b'"
    )


@pytest.mark.functions
@pytest.mark.views
@pytest.mark.django_db
def test_GetFunction(AdminUser, load_functions_to_database, api_client):
    client = api_client(AdminUser)

    load_functions_to_database()

    functions = Function.objects.all()

    url = f"http://localhost:8000/functions/{functions[0].id}/"

    response = client.get(url)

    res = response.json()

    assert res["name"] == "add_numbers"
    assert res["body"] == "def add_numbers(a,b):\n    return a + b"
    assert res["numberOfCalls"] == 0
    assert res["owner"] == AdminUser.id


@pytest.mark.functions
@pytest.mark.views
@pytest.mark.django_db
def test_Create_Update_Delete_Function(AdminUser, api_client):
    # Create
    client = api_client(AdminUser)

    url = "http://localhost:8000/functions/create/"
    data = {
        "name": "find_min",
        "body": "def find_min(nums):\n    return min(nums)",
        "numberOfCalls": 0,
    }
    response = client.post(url, data, format="json")

    res = response.json()

    assert res["name"] == data["name"]
    assert res["body"] == data["body"]
    assert res["numberOfCalls"] == data["numberOfCalls"]
    assert res["owner"] == AdminUser.id

    # Update.
    function_id = res["id"]

    url = f"http://localhost:8000/functions/update/{function_id}/"
    data = {
        "name": "find_min",
        "body": "def find_min(numbers):\n    return min(numbers)",
        "numberOfCalls": 0,
    }
    response = client.put(url, data, format="json")

    res = response.json()

    assert res["name"] == data["name"]
    assert res["body"] == data["body"]
    assert res["numberOfCalls"] == data["numberOfCalls"]

    function = Function.objects.get(id=function_id)

    assert function.name == data["name"]
    assert function.body == data["body"]
    assert function.numberOfCalls == data["numberOfCalls"]
    assert function.owner == AdminUser

    # Delete.
    url = f"http://localhost:8000/functions/delete/{function_id}/"
    response = client.delete(url)
    function = Function.objects.filter(id=function_id)

    assert function.count() == 0
