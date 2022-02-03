from django.test import TestCase
from ..models import CustomUser


class UserModelTest(TestCase):
    """ Test module for Custom User model """

    def setUp(self):
        CustomUser.objects.create(
            email='project@project.com',first_name='ashish', last_name='mate')
        CustomUser.objects.create(
            email='project2@project.com', first_name='mate', last_name='hello')

    def test_experiment_email(self):
        experiment_project = CustomUser.objects.get(first_name='ashish')
        experiment_project_2 = CustomUser.objects.get(first_name='mate')
        self.assertEqual(
            experiment_project.get_email(), "ashish belongs to project@project.com email.")
        self.assertEqual(
            experiment_project_2.get_email(), "mate belongs to project2@project.com email.")



