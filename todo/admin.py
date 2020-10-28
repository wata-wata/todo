from todo.models import TodoModel
from django.contrib import admin
from .models import TodoModel

# Register your models here.

# 管理画面でデータを扱えるようにする
admin.site.register(TodoModel)