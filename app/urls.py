from django.urls import path
from .views import TodoApi, todo_page

urlpatterns = [
    path('/', todo_page, name='todo-page'),
    path('/api/', TodoApi.as_view()),
    path('/api/<str:_id>', TodoApi.as_view(), name='_id')
]