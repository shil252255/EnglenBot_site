import random
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *


class WordSerializer(serializers.ModelSerializer):
    """
    Пока расположил его тут для простоты, потом перенесу его. (Если он вообще мне понадобиться)
    """
    class Meta:
        model = Words
        fields = ['pk', 'word', 'def_translations', 'word_class', 'past_form', 'past_participle', 'short']


class RandomWord(APIView):
    """
    Простая функция, для того чтобы проверить работу API.
    """
    def get(self, *args, **kwargs):
        all_words = Words.objects.all()
        random_word = random.choice(all_words)
        serialized_random_word = WordSerializer(random_word, many=False)
        return Response(serialized_random_word.data)


