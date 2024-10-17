from .views import GetTodos, UpdateTodo, DeleteTodo
from django.urls import path

urlpatterns = [
    path("",GetTodos.as_view(),name='home'),
    path('todo/<int:todo_id>/', UpdateTodo.as_view(),name='update_todo'),
    path('todo/<int:todo_id>/delete/', DeleteTodo.as_view(),name='delete_todo'),
    
]