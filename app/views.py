from django.http import JsonResponse, HttpRequest
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Todo


@method_decorator(csrf_exempt, name='dispatch')
class TodoApi(View):

    def get(self , request: HttpRequest , *args , **kwargs):
        if '_id' in kwargs:
            return self.get_one(request, kwargs['_id'])
        else: 
            return self.get_all(request)

    def get_all(self, request):
        todos = Todo.objects.all()
        dictTodos = [todo.to_dict() for todo in todos ]
        return JsonResponse(dictTodos,safe=False)
    
    def get_one(self, request , _id):
        todo = Todo.objects.get(id=_id)
        return JsonResponse(todo.to_dict())

    def post(self,request: HttpRequest):
        reqTodo = json.loads(request.body)
        newTodo = Todo.objects.create(
            title=reqTodo['title'],
            description= reqTodo['description']
        )
        return JsonResponse({'message': 'post request made', 'todo': newTodo.to_dict()})
    
    def delete(self , request: HttpRequest, *args , **kwargs):
        todoId = self.kwargs['_id']
        todo = Todo.objects.get(id=todoId)
        todo.delete()
        return JsonResponse({'message': f"deleted todo with id {todoId}", "Deleted todo" : todo.to_dict() })
    
    def put(self , request: HttpRequest, *args , **kwargs):
        todoId = self.kwargs['_id']
        newTodo = json.loads(request.body)
        todo = Todo.objects.get(id=todoId)
        todo.title = newTodo.get('title', todo.title)
        todo.description = newTodo.get('description', todo.description)
        todo.save()

        return JsonResponse({'message': f"updated todo with id {todoId}", "updated todo" : todo.to_dict() })
    
