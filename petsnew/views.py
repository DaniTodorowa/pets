from django.shortcuts import render

from django.shortcuts import render, redirect

from petsnew.models import Pet


def list_pets(request):
    context = {
        'pets': Pet.objects.all(),

    }
    return render(request, 'pets/pets_list.html', context)


def show_pet_details(request, pk):
    context = {
        'pet': Pet.objects.get(pk=pk),

    }
    return render(request, 'pets/pets_details.html', context)


def like_pet(request):
    return redirect('')

