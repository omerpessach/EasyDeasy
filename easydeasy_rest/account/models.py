from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from api.models import Disease, Article


class MyAccountManager(BaseUserManager):
    """
    This is a custom account manager which is responsible for managing creating of new accounts models.

    We manage the creation of normal and super user here!
    """

    def create_user(self, email, username, password=None):
        """
        Creating normal users
        :return: The new created user
        """

        if not email:
            raise ValueError('User must have email!')
        if not username:
            raise ValueError('User must have username!')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creating super user
        :return: The new created super user
        """
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    """
    This model is representing our custom account user model.

    *IMPORTANT*
    This user is authenticated with Email & Password.
    """

    email = models.EmailField(verbose_name='email', max_length=64, unique=True)
    username = models.CharField(max_length=32)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    # Our own custom fields
    has_agreed_to_terms = models.BooleanField(default=True)
    followed_diseases = models.ManyToManyField(Disease, blank=True)
    saved_articles = models.ManyToManyField(Article, blank=True)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_level):
        return True

    def __str__(self):
        return f'{self.username}'

