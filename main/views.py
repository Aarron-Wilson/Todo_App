from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Todo
from .models import Person
from .models import Catagory
from .forms import TodoForm
from django.views.decorators.csrf import csrf_exempt

def main_page(request):
    alltodos = Todo.objects.all()
    return render(request,'hello.html',{'name':'Aarron','alltodos':alltodos})

def addCatagory(request):
    return render(request,'createCatagory.html',{})

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'createTodo.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.Finished = False
        return super().form_valid(form)

def testAdd(request):
    try:
        newCatagory = Catagory( Name='Purchases')
        newCatagory.save()
        return JsonResponse({'result': 'all good'})
    except Exception as e:
        return JsonResponse({'result': 'error'})
@csrf_exempt
def todoCompleteToggle(request,todoID):
    todo = Todo.objects.get(pk=todoID)
    todo.Finished = not todo.Finished
    todo.save()
    return JsonResponse({'completed':todo.Finished})

@csrf_exempt
def deleteTodo(request,todoID):
    todo = Todo.objects.get(pk=todoID)
    todo.delete()
    return JsonResponse({'completed':True})

@csrf_exempt
def createCatagory(request,catagoryName):
    try:
        newCatagory = Catagory( Name=catagoryName)
        newCatagory.save()
        return JsonResponse({'completed': True})
    except Exception as e:
        return JsonResponse({'completed': False})

    