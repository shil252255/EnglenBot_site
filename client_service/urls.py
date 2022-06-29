from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('random_word/', RandomWord.as_view(), name='home'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
