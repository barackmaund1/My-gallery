from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Location
# Create your views here.
def index(request):
    images=Image.objects.all()
    locations=Location.get_locations()