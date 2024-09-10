from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. can be classes or functions
def home(request):
    return render(request,'index.html')
