from django.shortcuts import render, HttpResponse, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.
# All django view functions have to take a request as an argument
# they handle the request and always return HTTP response

# render main html template
def get_todo_list(request):
    # get all objects from item subgroup
    results = Item.objects.all()
    # render HTML page, passing request and item objects
    return render(request, "todo_list.html", {'items': results})

# function to render page to add item
def create_an_item(request):
    # check if POST method
    if request.method == "POST":
        
        # get form from forms.py file
        form = ItemForm(request.POST, request.FILES)
        # check if form is valid
        if form.is_valid():
            # save form and redirect to main page
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm()
    return render(request, "item_form.html", {'form': form})