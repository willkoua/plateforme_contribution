from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'plateforme_budgetaire.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('pages.urls', namespace="pages")),
    url(r'^members/', include('members.urls', namespace="members")),
    url(r'^projects/', include('projects.urls', namespace="projects")),

]