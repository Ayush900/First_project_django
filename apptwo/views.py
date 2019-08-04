from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'css_lev_two_assesment.html')
