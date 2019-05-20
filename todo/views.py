from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.
# All django view functions have to take a request as an argument
# they handle the request and always return HTTP response

# render html template
def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {'items': results})