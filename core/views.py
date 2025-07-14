import json
import os
from django.shortcuts import render, get_object_or_404
from .models import Profile, Prescription, MedicalHistory, Report
from django.conf import settings
from django.templatetags.static import static
from django.http import JsonResponse

def dashboard(request, profile_id=1):
    json_path = os.path.join(settings.BASE_DIR, 'sample_data.json')
    with open(json_path, encoding='utf-8') as f:
        data = json.load(f)

    tc_no = request.GET.get('tc_no', '').strip()
    profile = None
    prescriptions = []
    medications = data['medications']
    doctors = data['doctors']
    diagnoses = data['diagnoses']
    medical_histories = []
    reports = []
    latest_prescription = None
    previous_prescriptions = []
    profiles = data['profiles']

    if tc_no:
        # Find profile
        profile = next((p for p in data['profiles'] if p['tc_no'] == tc_no), None)
        if profile:
            prescriptions = [p for p in data['prescriptions'] if p['profile_tc_no'] == tc_no]
            if prescriptions:
                latest_prescription = next((p for p in prescriptions if p.get('is_latest')), prescriptions[-1])
                previous_prescriptions = [p for p in prescriptions if not p.get('is_latest')]
            medical_histories = [h for h in data['medical_histories'] if h.get('profile_tc_no') == tc_no]
            reports = [r for r in data['reports'] if r.get('profile_tc_no') == tc_no]

    context = {
        'profile': profile,
        'latest_prescription': latest_prescription,
        'previous_prescriptions': previous_prescriptions,
        'medications': medications,
        'doctors': doctors,
        'diagnoses': diagnoses,
        'medical_histories': medical_histories,
        'reports': reports,
        'today': '14 Temmuz 2025',
        'tc_no': tc_no,
        'profiles': profiles,
    }
    return render(request, 'core/dashboard.html', context)

def sample_data_json(request):
    json_path = os.path.join(settings.BASE_DIR, 'sample_data.json')
    with open(json_path, encoding='utf-8') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)
