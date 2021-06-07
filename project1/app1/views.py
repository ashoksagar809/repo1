from django.shortcuts import render
from django.http import HttpResponse
def wish(request):
    message="hello django students"
    return HttpResponse(message)
