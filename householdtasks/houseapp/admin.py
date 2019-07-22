from django.contrib import admin
from .models import Category, Status, Task, TaskLog, Priority

# Register your models here.
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Priority)
admin.site.register(Task)
admin.site.register(TaskLog)

