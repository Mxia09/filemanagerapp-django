from django.shortcuts import render
from django.http import HttpResponse
from interface.models import uploadedFiles

def index(request):
    latest_file_list = uploadedFiles.objects.order_by("id")
    return HttpResponse(latest_file_list)
def upload(request, upload):
    return HttpResponse("file is uploaded here %s." % upload)
def fileDetailed(request, fileDetailed):
    return HttpResponse("view file in more detail %s." % fileDetailed)