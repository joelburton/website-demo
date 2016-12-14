from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views import generic

from .models import Project


class ProjectListView(generic.ListView):
    """General list of project"""

    model = Project


class ProjectDetailView(generic.DetailView):
    """Detail page for a project."""

    model = Project


class ProjectCreateView(PermissionRequiredMixin,
                        generic.CreateView):
    """Create view for project."""

    permission_required = "planner.add_project"
    model = Project
    fields = ['id', 'title', 'description', 'website_url']

    def get_success_url(self):
        """Adding succeeded; report success at redirect."""

        messages.add_message(self.request,
                             messages.SUCCESS,
                             "Yay! Saved!")
        return reverse("project_list")

