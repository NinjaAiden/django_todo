from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.
# All django view functions have to take a request as an argument
# they handle the request and always return HTTP response

# render html template
def get_todo_list(request):
    # get all objects from item subgroup
    results = Item.objects.all()
    # render HTML page, passing request and item objects
    return render(request, "todo_list.html", {'items': results})