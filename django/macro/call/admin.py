from django.contrib import admin
from .models import School, Subject,Teacher

# Register your models here.
admin.site.register(School)
admin.site.register(Subject)
admin.site.register(Teacher)