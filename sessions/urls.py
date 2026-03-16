from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', lambda req: HttpResponse('sessions coming soon'), name='sessions-home'),
]