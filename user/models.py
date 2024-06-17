from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models



class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""

        if username is None:
            raise TypeError("User must have an username.") 
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have an email.')

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(email=email, username=username,  **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **kwargs):
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)

    USERNAME_FIELD = 'email'  # for login
    REQUIRED_FIELDS = ['username']  # for register a new acccount

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"


    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

