import json
from django.shortcuts import render, redirect
from landlord.models import Akeray
from django.contrib.auth import login
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def search(request):
    query = request.GET.get('query')
    akerays = Akeray.objects.filter(Q(title__icontains=query) | Q(location__icontains=query) | Q(summary__icontains=query) | Q(subcity__icontains=query))

    context = {
        'query': query,
        'akerays': akerays
    }

    return render(request, 'search.html', context)

def home(request):
    
    akerays = Akeray.objects.all()

    context = {
        'akerays': akerays
    }
    return render(request, 'home.html', context)

def tekeray(request):
    
    akerays = Akeray.objects.all()

    context = {
        'akerays': akerays
    }
    return render(request, 'tekeray.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/tekeray')
    
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})