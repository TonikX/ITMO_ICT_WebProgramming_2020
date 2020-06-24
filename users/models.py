from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, username: str, password: str):
        if username.lower().startswith("team"):
            ValueError("The username field must not starts with 'team'.")
        user = self.model(username=username)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

    def create_quest_maker(self, username: str, password: str):
        if username.lower().startswith("team"):
            ValueError("The username field must not starts with 'team'.")
        user = self.model(username=username)
        user.set_password(password)
        user.is_staff = True
        user.save()
        return user

    def create_team(self, password: str):
        user = self.model(username="team")
        user.set_password(password)
        user.save()
        user.username = f"team{user.id}"
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    is_superuser = models.BooleanField(
        'is_superuser',
        default=False
    )
    is_staff = models.BooleanField(
        'is_staff',
        default=False
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return self.username
