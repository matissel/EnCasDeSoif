from django.test import TestCase

# Create your tests here.
class SimpleTestCase(TestCase):
    def setUp(self):
        pass

    def test_allo(self):
            add = 1 + 1
            self.assertEqual(2, add)