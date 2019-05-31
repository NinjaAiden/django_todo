from django import forms
from .models import Item

# create a form template which requires an outer class and an inner class
# outer class takes form data as an input
# inner class takes data and structures it
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'done')