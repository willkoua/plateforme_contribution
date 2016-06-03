from django.db import models
from plateforme_contribution.behaviours import Timestampable
from members.models import Member

# Create your models here.
PROJECT_STATUS_CHOICES = (
    (u'En attente', 0),
    (u'Accepté', 1),
    (u'Rejeté', 2)
)


class Organization(Timestampable, models.Model):
    class Meta:
        verbose_name_plural = 'Organizations'

    name = models.CharField(
            verbose_name='Nom',
            max_length=255
    )

    logo = models.ImageField(
            upload_to="avatars_org",
            verbose_name='Logo',
            blank=True
    )

    url = models.URLField(
            verbose_name='URL',
            max_length=255,
            blank=True
    )

    def __str__(self):
        return self.name


class Project(Timestampable, models.Model):
    class Meta:
        verbose_name_plural = 'Projets'

    name = models.CharField(
            verbose_name='Nom du projet',
            max_length=255,
            blank=False,
            null=False
    )

    description = models.TextField(
            verbose_name='Description du projet'
    )

    status = models.CharField(
            verbose_name='Status',
            max_length=10,
            choices=PROJECT_STATUS_CHOICES,
    )

    creator = models.ForeignKey(
            Member,
            verbose_name='Creator',
            related_name='Projects'
    )

    organization = models.ForeignKey(
            Organization,
            verbose_name='Organization',
            related_name='projects'
    )

    def __unicode__(self):
        return self.name


class Contribution(Timestampable, models.Model):
    class Meta:
        verbose_name_plural = 'Contributions'

    description = models.TextField(
            verbose_name='Description du projet'
    )

    url = models.URLField(
            verbose_name='URL',
            max_length=255
    )

    project = models.ForeignKey(
            Project,
            verbose_name='Project',
            related_name='contributions',
    )

    creator = models.ForeignKey(
            Member,
            verbose_name='Creator',
            related_name='contributions'
    )

    def __str__(self):
        return self.name
