from django.conf.urls import url

from .views import ProjectListView, ProjectDetailView, ProjectCreateView

urlpatterns = [

    url(r'^$',
        ProjectListView.as_view(),
        name='project_list'),

    url(r'-new/$',
        ProjectCreateView.as_view(),
        name='project_create'),

    url(r'^(?P<pk>\d+)/$',
        ProjectDetailView.as_view(),
        name='project_detail'),

]