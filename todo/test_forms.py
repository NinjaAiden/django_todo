from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestToDoItemForm(TestCase):
    
    # tests must start with 'test_' or django won't detect them
    def test_can_create_an_item_with_just_name(self):
        form = ItemForm({'name': 'Create tests'})
        self.assertTrue(form.is_valid())
    
    def test_correct_message_for_missing_name(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])