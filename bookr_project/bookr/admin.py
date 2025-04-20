from django.contrib import admin

# Register your models here.
from .models import Project, Task, Book

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Book)