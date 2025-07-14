from django.contrib import admin
from .models import Profile, Prescription, MedicalHistory, Report, Doctor, Diagnosis, Medication

admin.site.register(Profile)
admin.site.register(Prescription)
admin.site.register(MedicalHistory)
admin.site.register(Report)
admin.site.register(Doctor)
admin.site.register(Diagnosis)
admin.site.register(Medication)
