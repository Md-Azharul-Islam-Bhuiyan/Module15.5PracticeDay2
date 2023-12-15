from django.shortcuts import render, redirect
from musician.forms import MusicianForm
from musician.models import MusicianModel

def add_musician(request):
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
            # print(musician_form.cleaned_data)
    else:
        musician_form = MusicianForm()
    return render(request, 'add_musician.html',{'form':musician_form})

def edit_musician(request, id):
    musician= MusicianModel.objects.get(pk=id)
    musician_form = MusicianForm(instance=musician)

    if request.method == 'POST':
        musician_form = MusicianForm(request.POST, instance= musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
            # print(musician_form.cleaned_data)
    return render(request, 'add_musician.html',{'form':musician_form})
