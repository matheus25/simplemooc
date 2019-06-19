from django.shortcuts import render
from .models import Course

# Create your views here.

def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)

def details(request, id):
    couses = Course.objects.get(id=id)
    template_name = 'couses/details.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)
