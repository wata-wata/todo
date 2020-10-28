from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 管理画面
    path('admin/', admin.site.urls),
    # adminでなければtodo.urlsを呼び出す
    path('', include('todo.urls')),
]
