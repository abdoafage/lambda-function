import pytest
from functions.models import Function
from functions.serializers import FunctionSerializer


@pytest.mark.functions
@pytest.mark.serializers
@pytest.mark.django_db
def test_function_serializer(AdminUser):
    function = FunctionSerializer(
        data={
            "name": "find_min",
            "body": "def find_min(nums):\n    return min(nums)",
            "numberOfCalls": 0,
            "runtime": "Python",
        }
    )
    function.is_valid(raise_exception=True)
    function.save(owner=AdminUser)

    assert Function.objects.count() == 1

    func = Function.objects.all()[0]

    assert func.name == "find_min"
    assert func.body == "def find_min(nums):\n    return min(nums)"
    assert func.numberOfCalls == 0
    assert func.owner == AdminUser
