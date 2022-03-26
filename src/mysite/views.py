from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return HttpResponse("Hello World!")

# about view function
def about_page(request):
   return render(request, 'about.html')