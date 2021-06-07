from django.shortcuts import render
from django.http import HttpResponse
def showIndex(request):
    message="hello django students"
    return HttpResponse(message)
