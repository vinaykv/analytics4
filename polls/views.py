#Author: Vinay vittal karagod
# Holds the various views to retrieve the data from the database
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import DTC

def index(request):
    latest_DTC_list = DTC.objects.order_by('-Dtc_timestamp')[:5]
    context = {'latest_DTC_list': latest_DTC_list}
    return render(request, 'polls/index.html', context)
	
def create(request,Dtc_code):
    return HttpResponse("You're looking at Dtc_code %s." % Dtc_code)
	
def detail(request, Dtc_code):
    response = "You're looking at the detail of DTC %s."
    return HttpResponse(response % Dtc_code)

def update(request, Dtc_code):
    return HttpResponse("You're updating on DTC %s." % Dtc_code)

def delete(request, Dtc_code):
    return HttpResponse("You're deleting the DTC record %s." % Dtc_code)