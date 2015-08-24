from django.shortcuts import render
from django.http import HttpResponse
from weight.models import Weight
from django.utils import timezone


def editorWeight(request):
    if request.method == 'POST':
        Weight.objects.create(weight=request.POST['weightInput'], record_date=timezone.now())

    all_weight = Weight.objects.all()
    return render(request, 'editorweight.html', {
        'new_weight': all_weight
    })
