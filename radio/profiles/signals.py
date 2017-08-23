from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import logging
from . import models
from django.contrib.auth import get_user_model

logger = logging.getLogger("project")
User = get_user_model()


@receiver(post_save, sender=User)
def create_profile_handler(sender, instance, created, **kwargs):
    if not created:
        return
    # Create the profile object, only if it is newly created
    profile = models.Profile(user=instance)
    profile.save()
    logger.info('New user profile for {} created'.format(instance))

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = models.Profile(user=user)
        profile.save()
