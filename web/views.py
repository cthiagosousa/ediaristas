from django.shortcuts import redirect, render
from .forms.diarist_form import DiaristForm
from .models import Diarist

def getAllDiarists(request):
    diarists = Diarist.objects.all()
    return render(request, 'list_diarists.html', {'diarists': diarists})

def createDiarist(request):
    if request.method == 'POST':
        form_diarist = DiaristForm(request.POST, request.FILES)

        if form_diarist.is_valid():
            form_diarist.save()
            return redirect('list-diarists')

    else:
        form_diarist = DiaristForm()
    
    return render(request, 'form_diarist.html', {'form_diarist': form_diarist})

def updateDiarist(request, id):
    diarist = Diarist.objects.get(id = id)
    if request.method == 'POST':
        form_diarist = DiaristForm(request.POST or None, request.FILES, instance=diarist)

        if form_diarist.is_valid():
            form_diarist.save()
            return redirect('list-diarists')
    else:
        form_diarist = DiaristForm(instance=diarist)
    
    return render(request, 'form_diarist.html', {'form_diarist': form_diarist})

def deleteDiarist(request, id):
    diarist = Diarist.objects.get(id = id)
    diarist.delete()
    return  redirect('list-diarists')
