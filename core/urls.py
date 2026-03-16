from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from core import views
from core import auth_view as my_auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('projects/', include('projects.urls')),
    path('sessions/', include('pomodoro_sessions.urls')),
    path('todos/', include('todos.urls')),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', my_auth_views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('export/', views.export_csv, name = 'export-csv'),
    
]