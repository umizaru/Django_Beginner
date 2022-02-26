from email import contentmanager
from multiprocessing import context
from shutil import register_unpack_format
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def top(request):
    context = {
        'name': 'たろう',
    }
    return render(request, 'myprofile/top.html', context)

def resume(request):
    return render(request, 'myprofile/resume.html')