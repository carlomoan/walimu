from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import jwt

# Create your models here.


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`. 

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email, firstname, surname, mobile, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # Each `User` needs a human-readable unique identifier that we can use to
    # represent the `User` in the UI. We want to index this column in the
    # database to improve lookup performance.
    username = models.CharField(db_index=True, max_length=255, unique=True)
    firstname = models.CharField(
        db_index=True, max_length=80, null=True, blank=True)
    surname = models.CharField(
        db_index=True, max_length=80, null=True, blank=True)

    # We also need a way to contact the user and a way for the user to identify
    # themselves when logging in. Since we need an email address for contacting
    # the user anyways, we will also use the email for logging in because it is
    # the most common form of login credential at the time of writing.
    email = models.EmailField(db_index=True, unique=True)

    # When a user no longer wishes to use our platform, they may try to delete
    # their account. That's a problem for us because the data we collect is
    # valuable to us and we don't want to delete it. We
    # will simply offer users a way to deactivate their account instead of
    # letting them delete it. That way they won't show up on the site anymore,
    # but we can still analyze the data.
    is_active = models.BooleanField(default=True)

    # The `is_staff` flag is expected by Django to determine who can and cannot
    # log into the Django admin site. For most users this flag will always be
    # false.
    is_staff = models.BooleanField(default=False)

    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    # More fields required by Django when specifying a custom user model.

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case we want it to be the email field.
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname', 'surname', 'email', 'mobile']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.username

    location = models.CharField(max_length=80, null=True, blank=True)
    mobile = models.CharField(max_length=12, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    institution = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=80, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.username


class Darasa(models.Model):
    title = models.CharField(max_length=30)
    syllabus = models.CharField(max_length=30, null=True, blank=True,)
    mitaala = models.ForeignKey(
        'Mitaala', null=True, blank=True, on_delete=models.CASCADE, related_name='mtaala_wa_darasa')


def __str__(self):
    return self.title


class Umahiri(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    mtaala = models.ForeignKey(
        'Mitaala', null=True, blank=True, on_delete=models.CASCADE)

def __str__(self):
    return self.title

class Umahsusi(models.Model):
    title = models.CharField(max_length=80, null=True, blank=True)
    competence = models.ForeignKey(
        'Umahiri', null=True, blank=True, on_delete=models.CASCADE)
    darasaname = models.ForeignKey(
        'Darasa', max_length=15, null=True, blank=True, on_delete=models.CASCADE)

def __str__(self):
    return self.title


class Muhula(models.Model):
    title = models.CharField(max_length=30)

def __str__(self):
    return self.title

class Juma(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)

def __str__(self):
    return self.title


class Siku(models.Model):
    title = models.CharField(max_length=30)
    week = models.ForeignKey(
        'Juma', null=True, blank=True, on_delete=models.CASCADE)
    term = models.ForeignKey(
        'Muhula', null=True, blank=True, on_delete=models.CASCADE)

def __str__(self):
    return self.title

class Shughuli(models.Model):
    title = models.CharField(max_length=80)
    vigezo = models.CharField(max_length=30)
    specific = models.ForeignKey(
        'Umahsusi', null=True, blank=True, on_delete=models.CASCADE)

def __str__(self):
    return self.title

class Vipindi(models.Model):
    title = models.CharField(max_length=50)
    maelezo = models.TextField(null=True, blank=True)
    muda = models.IntegerField(null=True, blank=True)
    vifaa = models.TextField(null=True, blank=True)
    day = models.ForeignKey(
        'Siku', null=True, blank=True, on_delete=models.CASCADE)
    activity = models.ForeignKey(
        'Shughuli', null=True, blank=True, on_delete=models.CASCADE)

def __str__(self):
    return self.title

class Mitaala(models.Model):
    title=models.CharField(max_length=60, null=True, blank=True)
    slug=models.SlugField()

    def __str__(self):
        return self.title

    class Meta:   
        verbose_name_plural = "mitaala"

class MtaalaArticles(models.Model):
    LEVEL_CHOICES = (
    ('parent','PARENT'),
    ('Level_1_child', 'LEVEL_1_CHILD'),
    ('Level_2_child', 'LEVEL_2_CHILD'),
    )
    title=models.CharField(max_length=255, null=True, blank=True)
    body=models.TextField(null=True, blank=True)
    slug=models.SlugField()
    parent=models.ManyToManyField("self", null=True, blank=True)
    headers=models.ForeignKey("MtaalaHead", blank=True,  on_delete=models.CASCADE)
    author=models.CharField(max_length=100, null=True, blank=True)
    level=models.CharField(max_length=50, choices=LEVEL_CHOICES, null=True, blank=True)

    class Meta:
        index_together = (('id', 'slug'),)

    def __str__(self):                           
        return self.title

    def get_header_list(self):
        k = self.headers # for now ignore this instance method   

        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

class MtaalaHead(models.Model):
    title=models.CharField(max_length=150, null=True, blank=True)
    slug=models.SlugField()
    mtaala=models.ForeignKey("Mitaala", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_mtaala_list(self):
        k = self.mtaala # for now ignore this instance method
