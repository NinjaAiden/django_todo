from django.test import TestCase

# Create your tests here.
class TestDjango(TestCase):
    
    # tests must start with 'test_' or django won't detect them
    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)