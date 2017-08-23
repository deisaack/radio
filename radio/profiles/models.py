from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)

    class Meta:
        abstract = True


class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)


class Rank(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Staff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    staff_no = models.CharField(max_length=20, unique=True)
    id_no = models.IntegerField(null=True, blank=True, unique=True)
    dob = models.DateField(null=True, blank=True)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (('m',MALE),('f',FEMALE))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    rank = models.ForeignKey(Rank, related_name='+')

    def __str__(self):
        return self.user.name
