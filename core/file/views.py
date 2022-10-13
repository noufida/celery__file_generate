from django.shortcuts import HttpResponse, render
from .task import generate_file
# Create your views here.



def file(request,file_name,data_count):
    #calling celery task
    generate_file.apply_async(kwargs={'file_name':file_name, 'data_count':data_count})
    #django returns a response to user immediately
    return HttpResponse('<h1>File generated successfully...</h1>') 