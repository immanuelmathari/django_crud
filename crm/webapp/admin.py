from django.contrib import admin

# Register your models here.

from . models import Record # we are in the same directory so we can use the dot
# You have to register your model
admin.site.register(Record)



