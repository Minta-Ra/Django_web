from django.http import HttpResponse
from django.shortcuts import render
from inventory.models import *

# These are like controllers

def index(request):

    # Get all artists from database
    artists = Artist.objects.all()

    # return HttpResponse("Hello world! Inventory Index"), locals() - does...
    return render(request, "inventory/index.html", locals())