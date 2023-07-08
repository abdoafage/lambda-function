from functions.models import Function


def test_load(AdminUser, load_functions_to_database):
    load_functions_to_database()
    assert Function.objects.count() == 4
