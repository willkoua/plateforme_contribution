from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns(
    '',
    url(
        r'^list/$',
        views.ProjectList.as_view(),
        name='project_list'
    ),
    url(
        r'^detail/(?P<pk>\d+)$',
        views.ProjectDetail.as_view(),
        name='project_detail'
    ),
)
