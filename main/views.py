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

def addPersonPage(request):
    return render(request,'createUser.html',{})

def editTodoPage(request,todoID):
    allPeople = Person.objects.all()
    allCatagorys = Catagory.objects.all()
    target = Todo.objects.get(pk=todoID)
    return render(request,'editTodo.html',{'todo':target,'allPeople':allPeople,'allCatagorys':allCatagorys})

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
    
@csrf_exempt
def createPerson(request,userName):
    try:
        newPerson = Person( Name=userName)
        newPerson.save()
        return JsonResponse({'completed': True})
    except Exception as e:
        return JsonResponse({'completed': False})

@csrf_exempt
def editTodo(request,todoID,person,catagory,description):
    try:
        wholeCatagory = Catagory.objects.get(Name=catagory)
        wholePerson = Person.objects.get(Name=person)
        targetTodo = Todo.objects.get(pk=todoID)
        targetTodo.AssignedPerson = wholePerson
        targetTodo.Catagory = wholeCatagory
        targetTodo.Description = description
        targetTodo.save()
        return JsonResponse({'completed':True})
    except Exception as e:
        print(e)
        return JsonResponse({'completed': False})