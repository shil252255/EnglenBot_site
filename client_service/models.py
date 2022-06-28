from django.db import models
import pytz

from .languages_list import LANGUAGES


class ServiceUser(models.Model):
    """
    Базовая информация о пользователях, пока решил не совмещать эту таблицу с пользователями джанго,
    не уверен, что так правильно, но пока мне так проще учитывая что пока доступ будет только из телеграмм.
    tg_id: id пользователя в телеграмме;
    first_name: по-умолчанию буду брать из телеграмм;
    last_name: дополнительно и необязательно, тоже из телеграмм;
    tg_username: тоже существует только по тому что могу получить эти данные;
    language: язык пользователя;
    timezone: часовой пояс пользователя основано на pytz, для того чтобы не присылать оповещения ночью (добавлю позже);
    registration_date: дата регистрации она же дата создания записи;
    role: роль пользователя, тоже для дальнейших доработок;
    is_delete: при удалении пользователя сохранять его данные;
    """
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    ROLES = (('admin', 'admin'), ('moderator', 'moderator'), ('user', 'user'))

    tg_id = models.BigIntegerField(unique=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    tg_username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='ru')
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    registration_date = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=ROLES, default='user')
    is_delete = models.BooleanField(default=False)
    password = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.first_name+self.last_name


class Words(models.Model):
    """
    Все слова, что есть в системе с наиболее популярными (или первыми добавленными) переводами.
    Пока поля word_class (часть речи), past_form (вторая форма неправильного глагола),
    past_participle (третья форма неправильного глагола) добавлены как заглушки на будущее.
    """
    word = models.CharField(max_length=200, unique=True)
    def_translations = models.CharField(max_length=200)
    word_class = models.CharField(max_length=200, null=True, blank=True)
    past_form = models.CharField(max_length=200, null=True, blank=True)
    past_participle = models.CharField(max_length=200, null=True, blank=True)
    short = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.word


class Videos(models.Model):
    """Предполагаю создание словарей на основе видео"""
    url = models.URLField()
    name = models.CharField(max_length=200, )
    chanel_name = models.CharField(max_length=200, null=True, blank=True)
    chanel_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Dicts(models.Model):
    """
    is_personal: создан ли этот словарь пользователем True или является частью платформы False;
    is_private: для созданных пользователем словарей, True - виден только пользователю создавшему словарь;
    is_changeable: можно ли изменять словарь рядовому пользователю, кроме создавшего его;
    """
    is_personal = models.BooleanField(default=True)
    video = models.ForeignKey(Videos, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(ServiceUser, on_delete=models.DO_NOTHING, related_name='created_by')
    changed_on = models.DateTimeField(auto_now=True)
    changed_by = models.ForeignKey(ServiceUser, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    is_private = models.BooleanField(default=True)
    is_changeable = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class WordsToDicts(models.Model):
    """
    Связь словарей со словами.
    serial_number: порядковый номер для словарей в которых это важно;
    personal_translation: поле для переопределения перевода для конкретного словаря;
    """
    word = models.ForeignKey(Words, on_delete=models.CASCADE)
    dictionary = models.ForeignKey(Dicts, on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=True, blank=True)
    personal_translation = models.CharField(max_length=200, null=True, blank=True)


class DictToUser(models.Model):
    """
    Взаимосвязь пользователей и словарей.
    is_activ: использовать ли слова из этого словаря для изучения;
    is_finish: изучен ли словарь полностью;
    """
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    dictionary = models.ForeignKey(Dicts, on_delete=models.CASCADE)
    is_activ = models.BooleanField(default=True)
    is_finish = models.BooleanField(default=False)


class UsersProgress(models.Model):
    """
    Прогресс пользователя в изучении слов.
    level: уровень изучения, используется для расчета даты следующей тренировки (0 - слово только что добавлено);
    next_training: дата следующей тренировки;
    """
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    word = models.ForeignKey(Words, on_delete=models.CASCADE)
    level = models.IntegerField()
    next_training = models.DateTimeField()


class Mistakes(models.Model):
    """
    Пока полностью не используется, функционал будет добавлен позднее.
    Предполагается сохранять все ошибки, чтобы находить наиболее сложные слова и
    наиболее частые неправильные ассоциации слов и подкидывать их чаще.
    """
    word = models.ForeignKey(Words, on_delete=models.CASCADE, related_name='word_with_mistakes')
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE, related_name='user_mistakes')
    answer = models.ForeignKey(Words, on_delete=models.CASCADE, related_name='wrong_answer')








