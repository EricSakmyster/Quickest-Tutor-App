from django.test import TestCase, RequestFactory
from django.urls import reverse, resolve
from .models import User, Category, TodoList
from .views import WelcomeView, tutorsearch, home
from .forms import TutorProfileForm, StudentProfileForm
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
        self.assertEquals('0000000000', testUser.phone)
    def testCreatedPhone(self):
        testUser=User.objects.get(first_name="Eric")
        testUser.phone='5005550000'
        self.assertEquals('5005550000', testUser.phone)
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

class viewTests(TestCase):

    def editSP_view (self):
        form_data = { 
                'year': 'new test blog',
                'phone': 'blog body',
                'classes': 'blog body',
                'major': 'blog body'

            } 
        form = StudentProfileForm(data= form_data) # create form instance 
        response = self.client.post('/home/editsp/', form_data)
        theUser = User.objects.get(year=form_data['year'])
        self.assertTrue(form.is_valid())
        self.assertEqual(theUser.year, 2)
        self.assertRedirects(response, '/home/studentProfile/',status_code=302, target_status_code=200)

    def editTP_view (self):
        form_data = { 
                'year': 'new test blog',
                'phone': 'blog body',
                'classes': 'blog body',
                'major': 'blog body', 
                'tsubjects': 'blog body',
                'texp':'blog body',
                'hourlyRate': 'blog body'
            } 

        form = TutorProfileForm(data= form_data) # create form instance 
        response = self.client.post('/home/edittp/', form_data)
        theUser = User.objects.get(year=form_data['year'])
        self.assertTrue(form.is_valid())
        self.assertEqual(theUser.year, 3)
        self.assertEqual(theUser.hourlyRate, 11)
        self.assertRedirects(response, '/home/tutorProfile/',status_code=302, target_status_code=200)


class testURLS(TestCase):

    def test_home_url(self):
        view = resolve('/home/')
        self.assertEquals(view.func, home)

    def test_signin_url(self):
        name = reverse('signin')
        path = '/home/signin' 
        self.assertEqual(name, path)

    def test_sProfile_url(self):
        name = reverse('profile')
        path = '/home/studentProfile' 
        self.assertEqual(name, path)

    def test_tProfile_url(self):
        name = reverse('tutorProfile')
        path = '/home/tutorProfile' 
        self.assertEqual(name, path)

    def test_sSchedule_url(self):
        name = reverse('schedule')
        path = '/home/studentSchedule' 
        self.assertEqual(name, path)

    def test_tSchedule_url(self):
        name = reverse('tutorSchedule')
        path = '/home/tutorSchedule' 
        self.assertEqual(name, path)

    def test_editSP_url(self):
        name = reverse('editSP')
        path = '/home/editSP' 
        self.assertEqual(name, path)

    def test_editTP_url(self):
        name = reverse('editTP')
        path = '/home/editTP' 
        self.assertEqual(name, path)

    def test_tSearch_url(self):
        name = reverse('tutorsearch')
        path = '/home/studentTutorSearch' 
        self.assertEqual(name, path)

    # def test_tAvailability_url(self):
    #     name = reverse('tutorProfileAvailibility')
    #     path = '/home/tutorProfileAvailibility' 
    #     self.assertEqual(name, path)