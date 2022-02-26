import imp
from pkgutil import ImpImporter
from django.contrib import admin
from .models import Diary

# Register your models here.
admin.site.register(Diary)
