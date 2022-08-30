
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Akeray, AkerayImage
from .forms import AkerayForm, ImageForm

# Create your views here.
def akeray_detail(request, id):

    akeray = get_object_or_404(Akeray, pk=id)

    imagesstring = "{ 'image': '%s' }," % (akeray.image.url)

    for image in akeray.images.all():
        imagesstring = imagesstring + ("{ 'image': '%s' }," % (image.image.url))

    return render(request, 'akeray_detail.html', context={'akeray': akeray, 'imagesstring': imagesstring})

@login_required
def add_akeray(request):
    if request.method == 'POST':

        form = AkerayForm(request.POST, request.FILES)
        files = request.FILES.getlist("image", request.user)
    
        if form.is_valid():
            f=form.save(commit=False)
            f.user = request.user
            f.save()

            for i in files:
                AkerayImage.objects.create(akeray=f, image=i)
            messages.success(request, "New rent added!")

            return HttpResponseRedirect("/tekeray")

        else:
            return (form.errors)

    else:
        form = AkerayForm()
        imageform = ImageForm()

    
        context = {
            'form': form,
            'imageform': imageform
        }
    return render(request, 'add_akeray.html', context)

@login_required
def update_akeray(request, akeray_id):
    akeray = get_object_or_404(Akeray, id=akeray_id)

    files = request.FILES.getlist("image")

    form = AkerayForm(request.POST or None, instance=akeray)

    if form.is_valid():
        f=form.save(commit=False)
        f.user == request.user
        f.save()
       
        for i in files:
            AkerayImage.objects.create(akeray=f, image=i)
        messages.success(request, "New rent added!")

        
        return HttpResponseRedirect("/")

    else:
        form = AkerayForm()
        imageform = ImageForm()
    
    context = {
        'form': form,
        'imageform': imageform
    }

    return render(request, 'update_akeray.html', context)




@login_required
def delete_akeray(request, akeray_id):
    akeray = get_object_or_404(Akeray, id = akeray_id)

    if request.user == akeray.user:

        Akeray.objects.filter(id=akeray_id).delete()
        return HttpResponseRedirect("/tekeray") 

    return render(request, "delete_akeray.html", {'akeray': akeray})
