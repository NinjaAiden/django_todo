"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# import function from views in todo subfolder
from todo.views import get_todo_list, create_an_item, edit_an_item, toggle_status

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # specify url for get_todo_list function
    # r identifies the following statement as a regular expression
    # ^$ identifies the route, variable name must be the same as a function name to be valid
    # ^ identifies start of the route expression
    # $ identifies the end of the route expression
    # removing either of these allows for extra routing to be placed before / after route name without recieving an error
    url(r'^$', get_todo_list),
    # 'add' is the url link
    url(r'^add$', create_an_item),
    # ?P tells the routing system that this is an expression
    # angular brackets bind the data to the query
    # '\d' is a regex for digit or int
    # adding a '+' allows for multiple digits instead of a single number
    url(r'^edit/(?P<id>\d+)$', edit_an_item),
    url(r'^toggle/(?P<id>\d+)$', toggle_status)
]
