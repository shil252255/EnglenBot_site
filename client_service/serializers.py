from rest_framework import serializers
from .models import *


class WordSerializer(serializers.ModelSerializer):
    """
    Сериализатор для слов.
    fields: расписаны так пока нет точного понимания что именно будет актуально в работе дольше.
    """
    class Meta:
        model = Words
        fields = ['pk', 'word', 'def_translations', 'word_class', 'past_form', 'past_participle', 'short']


