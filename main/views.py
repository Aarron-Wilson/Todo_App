from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Todo
from .models import Person
from .models import Catagory
from django.views.decorators.csrf import csrf_exempt

def main_page(request):
    alltodos = Todo.objects.all()
    return render(request,'hello.html',{'name':'Aarron','alltodos':alltodos})

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

    