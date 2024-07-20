from django.contrib import admin

# Register your models here.

from . models import Record # we are in the same directory
admin.site.register(Record)



