from django.urls import path
from . import views

urlpatterns = [
    path('start/<int:project_pk>/', views.start_session, name='start-session'),
    path('stop/<int:session_pk>/', views.stop_session, name='stop-session'),
    path('<int:session_pk>/', views.session_detail, name='session-detail'),
]