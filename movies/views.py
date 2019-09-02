from django.shortcuts import render
from .models import *

# Create your views here.

def index(request,template = 'index.html'):
	movies = Movie.objects.order_by('-in_theaters')
	return render(request, template, locals())
