from django.shortcuts import render, HttpResponse, redirect
from .models import Item

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
        # initialise new item
        new_item = Item()
        # get item's name and bind it to instance
        new_item.name = request.POST.get('name')
        # bind boolean done state to item
        new_item.done = 'done' in request.POST
        # save item to database
        new_item.save()
        
        return redirect(get_todo_list)
    return render(request, "item_form.html")