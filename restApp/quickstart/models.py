from time import timezone

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

import jwt

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())




class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)


#  New part on project's code
# class userProfile(models.Model):
#     username = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=128)
#     adminRole = models.BooleanField(default=False)

    # """
    # Определяет наш пользовательский класс User.
    # Требуется имя пользователя, адрес электронной почты и пароль.
    # """
    #
    # username = models.CharField(db_index=True, max_length=255, unique=True)
    #
    # email = models.EmailField(
    #     validators=[validators.validate_email],
    #     unique=True,
    #     blank=False
    #     )
    #
    # is_staff = models.BooleanField(default=False)
    #
    # is_active = models.BooleanField(default=True)
    #
    # # Свойство `USERNAME_FIELD` сообщает нам, какое поле мы будем использовать для входа.
    # USERNAME_FIELD = 'email'
    #
    # REQUIRED_FIELDS = ('username',)
    #
    # # Сообщает Django, что класс UserManager, определенный выше,
    # # должен управлять объектами этого типа.
    # objects = UserManager()
    #
    # def __str__(self):
    #     """
    #     Возвращает строковое представление этого `User`.
    #     Эта строка используется, когда в консоли выводится `User`.
    #     """
    #     return self.username
    #
    # @property
    # def token(self):
    #     """
    #     Позволяет нам получить токен пользователя, вызвав `user.token` вместо
    #     `user.generate_jwt_token().
    #
    #     Декоратор `@property` выше делает это возможным.
    #     `token` называется «динамическим свойством ».
    #     """
    #     return self._generate_jwt_token()
    #
    # def get_full_name(self):
    #     """
    #     Этот метод требуется Django для таких вещей,
    #     как обработка электронной почты.
    #     Обычно это имя и фамилия пользователя.
    #     Поскольку мы не храним настоящее имя пользователя,
    #     мы возвращаем его имя пользователя.
    #     """
    #     return self.username
    #
    # def get_short_name(self):
    #     """
    #     Этот метод требуется Django для таких вещей,
    #     как обработка электронной почты.
    #     Как правило, это будет имя пользователя.
    #     Поскольку мы не храним настоящее имя пользователя,
    #     мы возвращаем его имя пользователя.
    #     """
    #     return self.username
    #
    # def _generate_jwt_token(self):
    #     """
    #     Создает веб-токен JSON, в котором хранится идентификатор
    #     этого пользователя и срок его действия
    #     составляет 60 дней в будущем.
    #     """
    #     dt = datetime.now() + timedelta(days=60)
    #
    #     token = jwt.encode({
    #         'id': self.pk,
    #         'exp': int(dt.strftime('%s'))
    #     }, settings.SECRET_KEY, algorithm='HS256')
    #
    #     return token.decode('utf-8')


class userProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description=models.TextField(blank=True,null=True)
    location=models.CharField(max_length=30,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    is_organizer=models.BooleanField(default=False)
    adminRole = models.BooleanField(default=False)
    # username = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.user.username

class Card(models.Model):
    number = models.IntegerField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    balance = models.PositiveIntegerField()

class Log(models.Model):

    ACTION = [
        ('CREATE', 'Create new card'),
        ('BUY', 'Buy'),
        ('BONUS', 'Add bonus points'),
        ('SELL', 'Sell drink'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, blank=True)
    action = models.CharField(choices=ACTION, max_length=6)
    amount = models.PositiveIntegerField()
    timeDate = models.DateTimeField(auto_now=True)




