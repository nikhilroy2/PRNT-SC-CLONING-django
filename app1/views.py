from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def Index(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = GalleryForm()
    return render(request, 'app1/homepage/homepage.html',{"form": form})

