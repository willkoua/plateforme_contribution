from django.db import models
from plateforme_contribution.behaviours import Timestampable

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

    email = models.EmailField(
            verbose_name='Courriel',
    )

    username = models.CharField(
            verbose_name="Nom d'utilisateur",
            max_length=50,
    )

    def __str__(self):
        return self.email
