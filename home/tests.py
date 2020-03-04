from django.test import TestCase

# Create your tests here.
class StudentTab(TestCase):
    def test_updateSProfile(self):
        self.assertEqual(1,1)

    def test_updateSSchedule(self):
        self.assertEqual(1,1)

    def test_searchTutor(self):
        self.assertEqual(1, 1)

    def test_filterTutors(self):
        self.assertEqual(1,1)

class TutorTab(TestCase):
    def test_updateTProfile(self):
        self.assertEqual(1,1)

    def test_updateTSchedule(self):
        self.assertEqual(1,1)