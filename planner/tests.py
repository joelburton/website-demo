from django.test import TestCase

from planner.models import Project


class ProjectTestCase(TestCase):
    def setUp(self):
        self.p = Project.objects.create(title="Proj1", description="Descrip")
        self.tk1 = self.p.task_set.create(title="Task1", hours=2, done=False)
        self.tk2 = self.p.task_set.create(title="Task2", hours=3, done=True)

    def test_project(self):
        self.assertEqual(self.p.title, "Proj1")

    def test_total_hours(self):
        self.assertEqual(self.p.total_hours(), 2)
