from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project

@login_required
def project_list(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'projects/list.html', {'projects': projects})

@login_required
def project_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST.get('description', '')
        Project.objects.create(name=name, description=description, user=request.user)
        return redirect('project-list')
    return render(request, 'projects/create.html')

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    sessions = project.sessions.all().order_by('-start_time')
    running_session = project.sessions.filter(end_time__isnull=True).first()
    todos = running_session.todos.all() if running_session else []
    return render(request, 'projects/detail.html', {
        'project': project,
        'sessions': sessions,
        'running_session': running_session,
        'todos': todos,
    })

@login_required
def project_timer(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    session = project.sessions.filter(end_time__isnull=True).first()
    return render(request, 'timer.html', {
        'project': project,
        'session': session,
    })





