from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('test-slug')

def index2(request):
    return HttpResponse('test another slug')
