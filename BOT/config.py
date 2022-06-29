import os

from dotenv import load_dotenv

load_dotenv()
"""
Все приватные переменные я обычно храню в файле .env;
библиотека dotenv выгружает их в переменные окружения 
откуда я их уже и подтягиваю для работы в приложении.
"""

TELEGRAM_API_KEY = os.environ['TELEGRAM_API_KEY']
