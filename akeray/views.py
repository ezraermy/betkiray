from django.shortcuts import render, get_object_or_404, redirect
from .models import Renter, Category

# Create your views here.
def renter_detail(request, category_slug, slug):
    renter = get_object_or_404(Renter, slug=slug)

    context = {
        'renter': renter,
    }

    return render(request, 'renter_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    renters = category.renters.all()

    context = {
        'category': category,
        'renters': renters
    }
    
    return render(request, 'category_detail.html', context)

def add_rent(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        location = request.POST.get('location', '')
        contact = request.POST.get('contact', '')
        status = request.POST.get('status', '')

        new_rent = Renter.objects.create(name=name, location=location, contact=contact, status=status)

        return redirect('/home')