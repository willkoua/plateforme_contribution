from __future__ import unicode_literals

from django.db import models
from plateforme_contribution.behaviours import Timestampable
from django.contrib.auth.models import User


class Member(Timestampable, models.Model):
    class Meta:
        verbose_name_plural = 'Members'

    user = models.OneToOneField(
            User,
            related_name="member",
            verbose_name="User"
    )

    avatar = models.ImageField(
            verbose_name='Avatar',
            upload_to="avatars_user",
            blank=True,
            null=True
    )

    description = models.TextField(
            verbose_name='Description'
    )

    def __unicode__(self):
        return self.name
