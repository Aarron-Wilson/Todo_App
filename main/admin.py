from django.contrib import admin

from .models import Person
from .models import Catagory
from .models import Todo


# Register your models here.
admin.site.register(Person)
admin.site.register(Catagory)
admin.site.register(Todo)