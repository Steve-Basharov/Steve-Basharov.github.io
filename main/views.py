from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import job_form

def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
def job(request):
    error = ''
    if request.method == 'POST':
        form = job_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Not Valid'

    form = job_form()
    data = {
        'form':form
    }
    return render(request, 'main/zakaz.html', data)

