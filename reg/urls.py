from django.urls import path
from .views import *

urlpatterns = [
    path('', reg, name='login'),
    path('registration/', registration, name='registration'),
    ]