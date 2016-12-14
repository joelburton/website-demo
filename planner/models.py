from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Project(models.Model):
    """Project."""

    title = models.CharField(
        max_length=50,
        unique=True
    )

    description = models.TextField()

    website_url = models.URLField(
        blank=True,
    )

    image = models.ImageField(
        blank=True,
    )

    def __str__(self):
        return self.title

    def total_hours(self):
        """Total hours of all undone tasks."""

        undone_tasks = self.task_set.filter(done=False).all()

        return sum(t.hours for t in undone_tasks)

    def get_absolute_url(self):
        """URL for a project detail view."""

        return reverse("project_detail", kwargs={"pk": self.id})


class Task(models.Model):
    """Task for a project."""

    project = models.ForeignKey(Project)

    title = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        blank=True,
    )

    hours = models.PositiveSmallIntegerField(
        default=1,
    )

    done = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.title
