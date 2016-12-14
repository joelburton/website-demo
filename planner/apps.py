from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class PlannerConfig(AppConfig):
    name = 'planner'

    def ready(self):
        Project = self.get_model("Project")
        watson.register(Project)
