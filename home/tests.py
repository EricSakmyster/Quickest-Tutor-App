from django.test import TestCase, RequestFactory, Client
from django.urls import reverse, resolve
from .models import User, Category, TodoList
from .views import WelcomeView, home
from .forms import TutorProfileForm, StudentProfileForm, SessionRequestForm, TutorProfileAvailabilityForm
# Create your tests here.


class ModelTests(TestCase):
    def setUp(self):
        User.objects.create(first_name="Eric", last_name="Sakmyster")
        Category.objects.create(name="CS3240")
        Category.objects.create(name="CS2150")
        Category.objects.create(name="CS4102")
    def testUser(self):
        testUser=User.objects.get(first_name="Eric")
        self.assertTrue('Eric Sakmyster'==testUser.__str__())
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

class formTests(TestCase):
    
    def testSPForm (self):
        form = StudentProfileForm(data= { 
                'year': 1,
                'phone': '4444444444',
                'classes': 'CS 2150, CS 4102',
                'major': 'CS',
                'pfp': 'fire.jpg',

            }  
        )
        self.assertFalse(form.is_valid())
    def testSPForm2 (self):
        form = StudentProfileForm(data= { 
                'year': 5,
                'phone': '4444444444',
                'classes': 'CS 2150, CS 4102',
                'major': 'CS',

            }  
        )
        self.assertFalse(form.is_valid())
    def testSPForm3 (self):
        form = StudentProfileForm(data= { 
                'year': 1,
                'phone': '54444444444',
                'classes': 'CS 2150, CS 4102',
                'major': 'CS',

            }  
        )
        self.assertFalse(form.is_valid())
    def testSPForm4 (self):
        form = StudentProfileForm(data= { 
                'year': 1,
                'phone': 'phone number',
                'classes': 'CS 2150, CS 4102',
                'major': 'CS',

            }  
        )
        self.assertFalse(form.is_valid())
    def testTPForm (self):
        form = TutorProfileForm(data= { 
                'phone': '5555555555',
                'major': 'CS',
                'tsubjects': 'CS 2150, CS 4102',
                'texp': 'CS 2150 TA',
                'hourlyRate': '10',

            }  
        )
        self.assertFalse(form.is_valid())
    def testTPForm2 (self):
        form = TutorProfileForm(data= { 
                'phone': '55555555550',
                'major': 'CS',
                'tsubjects': 'CS 2150, CS 4102',
                'texp': 'CS 2150 TA',
                'hourlyRate': '10',

            }  
        )
        self.assertFalse(form.is_valid())
    def testSessionRequestForm1(self):
        form = SessionRequestForm(data={
            'tutor_username': 'bob',
            'course': 'CS 3240',
            'description': 'I need help learning Django.',
            'building': 'Rice Hall',
        })
        self.assertTrue(form.is_valid())
        
    def testTPAform1(self):
        form  = TutorProfileAvailabilityForm(data ={
                'available': '11/29/2000 12:30'
            }
        )
        self.assertTrue(form.is_valid())
    def testTPAform2(self):
        form  = TutorProfileAvailabilityForm(data ={
                'available': '2019/12/03 12:30'
            }
        )
        self.assertFalse(form.is_valid())

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