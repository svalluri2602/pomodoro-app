from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from pomodoro_sessions.models import Session
import csv
from django.http import HttpResponse



def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    today = timezone.now().date()
    week_start = today - timedelta(days=today.weekday())

    user_sessions = Session.objects.filter(
        project__user=request.user,
        end_time__isnull=False
    )

    # today's total
    today_sessions = user_sessions.filter(start_time__date=today)
    today_total =  sum((s.duration for s in today_sessions if s.duration), timedelta(0))
    # this week's total
    week_sessions = user_sessions.filter(start_time__date__gte=week_start)
    week_total =  sum((s.duration for s in week_sessions if s.duration), timedelta(0))

    # per project totals
    from projects.models import Project
    projects = Project.objects.filter(user=request.user)
    project_totals = []
    for project in projects:
        total = sum(
            (s.duration for s in user_sessions.filter(project=project) if s.duration),
    timedelta(0)
        )
        project_totals.append({'project': project, 'total': total})

    # streak logic
    streak = 0
    check_date = today
    while True:
        if user_sessions.filter(start_time__date=check_date).exists():
            streak += 1
            check_date -= timedelta(days=1)
        else:
            break

    return render(request, 'dashboard.html', {
        'today_total': today_total,
        'week_total': week_total,
        'project_totals': project_totals,
        'streak': streak,
    })


@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="sessions.csv"'

    writer = csv.writer(response)
    writer.writerow(['Project', 'Start Time', 'End Time', 'Duratioin', 'Todos'])

    sessions = Session.objects.filter(

        project__user = request.user,
        end_time__isnull = False
    ).order_by('-start_time')


    for session in sessions:
        todos = ', '.join(t.text for t in session.todos.all())
        writer.writerow([

        session.project.name, 
        session.start_time, 
        session.end_time,
        session.duration,
        todos,

        ])

        return response

