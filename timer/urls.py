from django.urls import path
from .views import TIMER

urlpatterns = [
    path('', TIMER.as_view())
]