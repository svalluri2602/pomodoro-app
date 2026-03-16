from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from projects.models import Project
from .models import Session

@login_required
def start_session(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    Session.objects.create(project=project)
    return redirect('project-detail', pk=project_pk)

@login_required
def stop_session(request, session_pk):
    session = get_object_or_404(Session, pk=session_pk)
    session.end_time = timezone.now()
    session.duration = session.end_time - session.start_time
    session.save()
    return redirect('project-detail', pk=session.project.pk)

@login_required
def session_detail(request, session_pk):
    session = get_object_or_404(Session, pk=session_pk)
    todos = session.todos.all()
    return render(request, 'pomodoro_sessions/session_detail.html', {
        'session': session,
        'todos': todos,
    })

