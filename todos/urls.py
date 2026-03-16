from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', lambda req: HttpResponse('Todos coming soon'), name='todos-home'),
    path('add/<int:session_pk>/', views.add_todo, name = 'add-todo'),
    path('toggle/<int:todo_pk>/',views.toggle_todo,name = 'toggle-todo'),
    path('delete/<int:todo_pk>/', views.delete_todo, name='delete-todo'),
]

