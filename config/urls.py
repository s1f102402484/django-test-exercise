"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.index, name='index'),
    path('en', todo_views.index, name='index'),
    path('<int:task_id>/', todo_views.detail, name='detail'),
    path('<int:task_id>/dalete',todo_views.delete,name='delete'),
    path('<int:task_id>/update',todo_views.update, name='update'),
    path('<int:task_id>/close', todo_views.close, name='close'),
    path('delete_complete/', todo_views.delete_complete, name='delete_complete'),
    path('ja/', todo_views.index_ja, name='index_ja'),
    path('<int:task_id>/ja/', todo_views.detail_ja, name='detail_ja'),
    path('<int:task_id>/dalete/ja/',todo_views.delete_ja,name='delete_ja'),
    path('<int:task_id>/update/ja/',todo_views.update_ja, name='update_ja'),
    path('<int:task_id>/close/ja/', todo_views.close_ja, name='close_ja'),
    path('delete_complete/ja/', todo_views.delete_complete, name='delete_complete_ja'),
]
