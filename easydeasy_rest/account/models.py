from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser


class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):

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


def get_profile_image_path(self) -> str:
    """
    Returns the path for the account profile image.
    :param self: Account
    :return: Path to it's account profile image
    """
    return f'profile_images/{self.pk}/{"profile_image.png"}'


def get_default_profile_image_path() -> str:
    """
    Returns the path for the default profile image.
    :return: Path to it's account profile image
    """
    return f'default_profile_image/default_profile_image.png'


class Account(AbstractBaseUser):

    email = models.EmailField(verbose_name='email', max_length=64, unique=True)
    username = models.CharField(max_length=32)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_path, null=True, blank=True,
                                      default=get_default_profile_image_path)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_level):
        return True

    def __str__(self):
        return f'{self.username}'

