from django.shortcuts import render, HttpResponse

# Create your views here.
# All django view functions have to take a request as an argument
# they handle the rrquest and always return HTTP response
def say_hello(request):
    return HttpResponse("Hello World")

