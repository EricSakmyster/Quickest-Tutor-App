
from django.test import TestCase, RequestFactory
from .models import User
from .views import WelcomeView, tutorsearch
# Create your tests here.
'''
class FunctionalityTests(TestCase):
    def setUp(self):
        self.factory=RequestFactory()
        
    def test_redirect_when_not_logged_in(self):
        request= self.factory.get('/studentTutorSearch')
        response = tutorsearch(request)
        self.assertEqual(response.status_code, 200)
class ModelTests(TestCase):
    def setUp(self):
        Student.objects.create(first_name="Eric", last_name="Sakmyster", year=2, phone="703-333-3333", classes="Math, Science", major="CS")
    def testStudent(self):
        testStudent = Student.objects.get(last_name="Sakmyster")
        self.assertTrue(testStudent.last_name==testStudent.__str__())
'''   
