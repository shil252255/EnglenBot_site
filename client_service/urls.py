from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('', api_info),
    path('random_word/', RandomWord.as_view(), name='random_word'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('add_tg_user/', TgUser.as_view(), name='add_tg_user')
]
