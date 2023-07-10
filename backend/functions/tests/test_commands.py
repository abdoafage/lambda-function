import pytest
from functions.models import Function


def test_load(AdminUser, load_functions_to_database):
    load_functions_to_database()
    assert Function.objects.count() == 4


@pytest.mark.django_db
def test_delete_null_owner(delete_null_onwer_function):
    function = Function.objects.create(
        name="find_min", body="def find_min(nums):\n    return min(nums)"
    )
    assert Function.objects.count() == 1
    assert function.owner is None

    delete_null_onwer_function()

    assert Function.objects.count() == 0
