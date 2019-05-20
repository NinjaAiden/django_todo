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

# import get_todo_list function from views in todo subfolder
from todo.views import get_todo_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # specify url for get_todo_list function
    # r identifies the following statement as a regular expression
    # ^$ identifies the route, variable name must be the same as a function name to be valid
    # ^ identifies start of the route expression
    # $ identifies the end of the route expression
    # removing either of these allows for extra routing to be placed before / after route name without recieving an error
    url(r'^$', get_todo_list)
]
