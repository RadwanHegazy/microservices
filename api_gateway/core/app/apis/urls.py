from .views import get, create, update, delete
from django.urls import path

urlpatterns = [
    path("v1/get/", get.GetTodos.as_view(), name="get_todos"),
    path('v1/create/', create.CreateTodo.as_view(),name='create_todo'),
    path("v1/get/<int:todo_id>/", get.GetTodo.as_view(), name="get_todo"),
    path("v1/update/<int:todo_id>/", update.UpdateTodo.as_view(), name="update_todo"),
    path("v1/delete/<int:todo_id>/", delete.DeleteTodo.as_view(), name="delete_todo"),
]