from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from .query import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def upload(request):
    if(request.method == 'POST'):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            pho = Photo(image=form.cleaned_data['image'])
            pho.save()
            raw,thumb = query(pho.image)
            rawstr = ','.join(raw)
            thumbstr = ','.join(thumb)
            context = {'raw':raw, 'thumb':thumb}
            return render(request, 'gallery.html', context)
    return HttpResponse('allow only allow POST')

def test(request):
    return render(request, 'test.html')
