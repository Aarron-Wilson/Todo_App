from django.urls import path
from . import views
from .views import TodoCreateView
from django.conf import settings
from django.conf.urls.static import static

#URL Conf
urlpatterns = [
    path('',views.main_page,name='home'),
    path('todo/edit/<int:todoID>',views.editTodoPage),
    path("api/",views.testAdd),
    path("api/todo/toggle/<int:todoID>",views.todoCompleteToggle),
    path("api/todo/edit/<int:todoID>/<str:person>/<str:catagory>/<str:description>",views.editTodo),
    path("api/todo/delete/<int:todoID>",views.deleteTodo),
    path("api/catagory/create/<str:catagoryName>",views.createCatagory),
    path("api/user/create/<str:userName>",views.createPerson),
    path('addTodo/',TodoCreateView.as_view(),name='todo_add'),
    path('addCatagory/',views.addCatagory),
    path('addPerson/',views.addPersonPage)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)