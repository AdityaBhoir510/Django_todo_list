from django.urls import path
from todoList_app.views import *

urlpatterns = [
    path('login',login.as_view()),
    path('register',register.as_view()),
    path('todo',todo.as_view()),
    path('delete/<id>',delete.as_view()),
    path('edit/<eid>',edit.as_view()),
]