from django.shortcuts import render, redirect, get_object_or_404
from .models import Materiel
from .forms import MaterielForm

def liste_materiels(request):
    materiels = Materiel.objects.all()
    return render(request, 'materiel/liste.html', {'materiels': materiels})

def ajouter_materiel(request):
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_materiels')
    else:
        form = MaterielForm()
    return render(request, 'materiel/form.html', {'form': form})

def modifier_materiel(request, id):
    materiel = get_object_or_404(Materiel, id=id)
    form = MaterielForm(request.POST or None, instance=materiel)
    if form.is_valid():
        form.save()
        return redirect('liste_materiels')
    return render(request, 'materiel/form.html', {'form': form})

def supprimer_materiel(request, id):
    materiel = get_object_or_404(Materiel, id=id)
    if request.method == 'POST':
        materiel.delete()
        return redirect('liste_materiels')
    return render(request, 'materiel/confirm_delete.html', {'materiel': materiel})
