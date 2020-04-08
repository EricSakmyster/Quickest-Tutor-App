
from django.test import TestCase, RequestFactory
from .models import User, Category, TodoList
from .views import WelcomeView, tutorsearch, home
# Create your tests here.

class FunctionalityTests(TestCase):
    def setUp(self):
        self.factory=RequestFactory()
        
    def test_redirect_when_not_logged_in(self):
        request= self.factory.get('/studentTutorSearch')
        response = tutorsearch(request)
        self.assertEqual(response.status_code, 200)
    '''
    def test_redirect_to_home_when_not_logged_in_(self):
        request1 = self.factory.get('/welcome')
        response1 = WelcomeView.as_view()(request1).render()
        request2 = self.factory.get('/home')
        response2 = home(request2)
        self.assertEquals(response1.content, response2.content)
    '''
class ModelTests(TestCase):
    def setUp(self):
        User.objects.create(first_name="Eric", last_name="Sakmyster")
        Category.objects.create(name="CS3240")
        Category.objects.create(name="CS2150")
        Category.objects.create(name="CS4102")
    def testUser(self):
        testUser=User.objects.get(first_name="Eric")
        self.assertTrue('Eric Sakmyster'==testUser.__str__())
    def testDefaultPhone(self):
        testUser=User.objects.get(first_name="Eric")
        self.assertEquals('000-000-0000', testUser.phone)
    def testCreatedPhone(self):
        testUser=User.objects.get(first_name="Eric")
        testUser.phone='500-555-0000'
        self.assertEquals('500-555-0000', testUser.phone)
    def testYear(self):
        testUser=User.objects.get(first_name="Eric")
        testUser.year='4'
        self.assertFalse('0'==testUser.year)
    def testCategory(self):
        testCategory=Category.objects.get(name="CS2150")
        self.assertEquals(testCategory.__str__(), "CS2150")
    def testCategory2(self):
        count=0
        for i in Category.objects.all():
            count+=1
        self.assertEquals(3, count)


