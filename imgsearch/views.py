from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def upload(request):
    if(request.method == 'POST'):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            pho = Photo(image=form.cleaned_data['image'])
            pho.save()
            return HttpResponse('image upload success')
    return HttpResponse('allow only allow POST')
