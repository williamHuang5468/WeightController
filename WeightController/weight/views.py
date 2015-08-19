from django.shortcuts import render
from django.http import HttpResponse

def editorWeight(request):
	return render(request, 'editorweight.html', {
		'new_weight':request.POST.get('weightInput','')
	})