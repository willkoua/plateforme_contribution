from django.contrib import admin
from projects.models import Project, Organization, Contribution

admin.site.register(Project)
admin.site.register(Organization)
admin.site.register(Contribution)
