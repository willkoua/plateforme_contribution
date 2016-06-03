# coding: utf-8

from django.views import generic
from projects.models import Project, PROJECT_STATUS_CHOICES


class ProjectList(generic.ListView):
    # List all project
    template_name = 'projects/list.html'
    context_object_name = 'projects'

    def dispatch(self, *args, **kwargs):
        return super(ProjectList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        status = PROJECT_STATUS_CHOICES[1][0]
        print(status)
        list_project = Project.objects.filter(
            status=status
        ).order_by('-create_date')

        return list_project
