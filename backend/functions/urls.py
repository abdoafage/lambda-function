from django.urls import path
from .views import (
    GetAllFunctions,
    GetFunction,
    CreateFunction,
    RunFunction,
    TestFunction,
    UpdateFunction,
    DeleteFunction,
)


urlpatterns = [
    path("", GetAllFunctions.as_view(), name="GetAllFunctions"),
    path("create/", CreateFunction.as_view(), name="CreateFunctions"),
    path("update/<uuid:id>/", UpdateFunction.as_view(), name="UpdateFunction"),
    path("delete/<uuid:id>/", DeleteFunction.as_view(), name="DeleteFunction"),
    path("<uuid:id>/", GetFunction.as_view(), name="GetFunctions"),
    path("run/<uuid:id>/", RunFunction.as_view(), name="RunFunction"),
    path("test/<uuid:id>/", TestFunction.as_view(), name="TestFunction"),
]
