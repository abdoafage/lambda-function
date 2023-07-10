from functions.models import Function


def test_function_model(AdminUser, create_user_obj):
    simpleUser = create_user_obj(username="simpleUser", password="password")

    func1 = Function.objects.create(
        name="find_max",
        body="def find_max(nums):\n    return max(nums)",
        owner=AdminUser,
    )

    func2 = Function.objects.create(
        name="find_min",
        body="def find_min(nums):\n    return min(nums)",
        owner=simpleUser,
    )

    assert func1.name == "find_max"
    assert func1.body == "def find_max(nums):\n    return max(nums)"
    assert func1.numberOfCalls == 0
    assert func1.owner == AdminUser
    assert func1.owner.username == "admin"

    assert func2.name == "find_min"
    assert func2.body == "def find_min(nums):\n    return min(nums)"
    assert func2.numberOfCalls == 0
    assert func2.owner == simpleUser
    assert func2.owner.username == "simpleUser"

    assert Function.objects.count() == 2
