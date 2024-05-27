from django.urls import path
from . import views
from .views import TodoCreateView
from django.conf import settings
from django.conf.urls.static import static

#URL Conf
urlpatterns = [
    path('',views.main_page,name='home'),
    path("api/",views.testAdd),
    path("api/todo/toggle/<int:todoID>",views.todoCompleteToggle),
    path('addTodo/',TodoCreateView.as_view(),name='todo_add')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)