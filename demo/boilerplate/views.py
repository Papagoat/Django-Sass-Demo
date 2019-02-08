from django.shortcuts import render

from .models import Demo

def index(request):
    latest_demo_list = Demo.objects.all()
    context = {'latest_demo_list': latest_demo_list}
    return render(request, 'boilerplate/index.html', context)
