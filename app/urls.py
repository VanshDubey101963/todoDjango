from django.urls import path
from .views import TodoApi

urlpatterns = [
    path('', TodoApi.as_view()),
    path('<str:_id>', TodoApi.as_view(), name='_id')
]
