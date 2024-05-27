from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#URL Conf
urlpatterns = [
    path('',views.main_page),
    path("api/",views.testAdd),
    path("api/todo/toggle/<int:todoID>",views.todoCompleteToggle)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)