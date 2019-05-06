from django.test import TestCase

# Create your tests here.


class SimpleTestCase2(TestCase):
    def setUp(self):
        pass

    def test_1(self):
        add = 1 + 1
        self.assertEqual(2, add)
