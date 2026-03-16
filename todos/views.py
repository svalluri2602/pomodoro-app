from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from pomodoro_sessions.models import Session
from .models import Todo

# Create your views here.


@login_required

def add_todo(request, session_pk):
    session = get_object_or_404(Session, pk = session_pk)
    if request.method == 'POST':
        text = request.POST.get('text','').strip()
        if text:
            Todo.objects.create(session=session, text=text)
        
    return redirect('project-detail', pk=session.project.pk)


@login_required

def toggle_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('project-detail', pk = todo.session.project.pk)


@login_required
def delete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    project_pk = todo.session.project.pk
    todo.delete()
    return redirect('project-detail', pk=project_pk)







