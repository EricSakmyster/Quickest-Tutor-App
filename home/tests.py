from django.test import TestCase

# Create your tests here.
class StudentTab(TestCase):
    def updateSProfile(self):
        self.assertEqual(1,1)

    def updateSSchedule(self):
        self.assertEqual(1,1)

    def searchTutor(self):
        self.assertEqual(1, 1)

    def filterTutors(self):
        self.assertEqual(1,1)

class TutorTab(TestCase):
    def updateTProfile(self):
        self.assertEqual(1,1)

    def updateTSchedule(self):
        self.assertEqual(1,1)