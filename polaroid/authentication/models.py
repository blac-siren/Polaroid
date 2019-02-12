from django.db import models
from django.core.validators import validate_email
from core.model import TimestampedModel
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.contrib.auth.models import User


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves user with given usernames, email, password
        """
        if not username:
            raise ValueError("User must have username")

        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        validate_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email)
        user.set_password(password)

        user.save()

        return user

    def authenticate(self, email=None, password=None):
        print(email)

        user = User.objects.get(email=email)
        print(user)

        if not user:
            return None
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password')

        user = self.create_user(username, email, password)
        user.is_super = True
        user.is_staff = True
        user.save()

        return user



class User(AbstractBaseUser, TimestampedModel, PermissionsMixin, UserManager):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
