from django.shortcuts import render

def homepage(request):
    return render(request, 'management/homepage.html', {})

# Create your views here.
