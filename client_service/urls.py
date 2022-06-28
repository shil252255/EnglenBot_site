from django.urls import path
from .views import *

urlpatterns = [
    path('random_word/', RandomWord.as_view(), name='home'),
]
