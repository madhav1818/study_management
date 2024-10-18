from django.shortcuts import render, redirect, get_object_or_404
from .models import Study

def study_list(request):
    studies = Study.objects.all()
    return render(request, 'study_management/study_list.html', {'studies': studies})

def study_add(request):
    if request.method == 'POST':
        study_name = request.POST['study_name']
        study_phase = request.POST['study_phase']
        sponsor_name = request.POST['sponsor_name']
        study_description = request.POST['study_description']
        
        Study.objects.create(
            study_name=study_name,
            study_phase=study_phase,
            sponsor_name=sponsor_name,
            study_description=study_description
        )
        
        return redirect('study_list')
    
    sponsor_names = Study.objects.values_list('sponsor_name', flat=True).distinct()
    
    return render(request, 'study_management/study_add.html', {'sponsor_names': sponsor_names})

def study_edit(request, study_id):
    study = get_object_or_404(Study, id=study_id)
    if request.method == 'POST':
        study.study_name = request.POST['study_name']
        study.study_phase = request.POST['study_phase']
        study.sponsor_name = request.POST['sponsor_name']
        study.study_description = request.POST['study_description']
        study.save()
        return redirect('study_list')
    return render(request, 'study_management/study_edit.html', {'study': study})

def study_delete(request, id):
    study = get_object_or_404(Study, id=id)
    study.delete()
    return redirect('study_list')

def study_view(request, study_id):
    study = get_object_or_404(Study, id=study_id)
    return render(request, 'study_management/study_view.html', {'study': study})

def study_delete_multiple(request):
    if request.method == "POST":
        study_ids = request.POST.getlist('study_selection')
        Study.objects.filter(id__in=study_ids).delete()
        return redirect('study_list')
