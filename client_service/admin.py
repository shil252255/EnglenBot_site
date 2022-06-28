from django.contrib import admin
from .models import *


@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'word', 'def_translations']

