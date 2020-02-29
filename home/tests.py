from django.test import TestCase

# Create your tests here.
class DummyTest(TestCase):
    def test1(self):
        self.assertEqual(1,1)

class DummyTest2(TestCase):
    def test2(self):
        self.assertEqual(2,2)