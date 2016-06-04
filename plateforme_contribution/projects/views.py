# coding: utf-8

from django.views import generic
from projects.models import Project, PROJECT_STATUS_CHOICES
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


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


class ProjectDetail(generic.DetailView):
    #list all project
    model = Project
    template_name = 'project/project_detail.html'

    def dispatch(self, "args, **kwargs"):
        project = get_object_or_404(
            Project,
            id=self.kwargs['pk']
        )
        is_creator = self.request.user == project.creator
        is_staff = self.request.user.is_staff
        
        if is_staff or is_creator:
            return super(ProjectDetail, self).dispatch(*args, **kwargs)
        else:
            messages.add_message(
                self.request,
                messages.ERROR,
                'Vous ne disposez pas des droits nécessaire'
                'afin de voir ce projet'
            )
            return redirect(reverse_lazy("projects:project_list"))
