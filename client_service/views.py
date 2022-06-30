import random
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


def api_info(request):
    return render(request, 'client_service/API_Info.html')


class RandomWord(APIView):
    """
    Простая функция, для того чтобы проверить работу API.
    """
    def get(self, *args, **kwargs):
        all_words = Words.objects.all()
        random_word = random.choice(all_words)
        serialized_random_word = WordSerializer(random_word, many=False)
        return Response(serialized_random_word.data)


class TgUser(APIView):
    """
    Добавление пользователя телеграмм при помощи бота.
    """
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass
