from django.contrib import admin
from .models import Campus, Stream, Facility, Course, Lab, Subject, Faculty, Students_data

admin.site.register(Campus)
admin.site.register(Stream)
admin.site.register(Facility)
admin.site.register(Course)
admin.site.register(Lab)
admin.site.register(Subject)
admin.site.register(Faculty)
admin.site.register(Students_data)

# Register your models here.
