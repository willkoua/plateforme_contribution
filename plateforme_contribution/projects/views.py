# coding: utf-8

from django.views import generic
from projects.models import Project, Contribution
from django.shortcuts import render, redirect, get_object_or_404
import markdown


class ProjectList(generic.ListView):
    # List all project
    template_name = 'projects/list.html'
    context_object_name = 'projects'

    def dispatch(self, *args, **kwargs):
        return super(ProjectList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        # status = PROJECT_STATUS_CHOICES[1][0]
        # print(status)
        list_project = Project.objects.order_by('-create_date')

        return list_project


class ProjectDetail(generic.DetailView):
    # List all project
    model = Project
    template_name = 'projects/detail.html'

    def dispatch(self, *args, **kwargs):
        project = get_object_or_404(
            Project,
            id=self.kwargs['pk']
        )
        return super(ProjectDetail, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        md = markdown.Markdown()
        context['content_html'] = md.convert(self.object.description)
        return context


class ContributionCreate(generic.CreateView):
    model = Contribution
    template_name = 'contributions/create.html'
    fields = "__all__"
