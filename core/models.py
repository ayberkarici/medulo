from django.db import models
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tc_no = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField(blank=True)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    diploma_no = models.CharField(max_length=20)
    branch = models.CharField(max_length=100)

class Diagnosis(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)

class Medication(models.Model):
    name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=20)
    dosage = models.CharField(max_length=20)
    period = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=20)

class Prescription(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    protocol_no = models.CharField(max_length=20, default='000000')
    provision_type = models.CharField(max_length=20, default='Normal')
    prescription_type = models.CharField(max_length=20, default='Normal')
    prescription_subtype = models.CharField(max_length=20, default='Ayaktan')
    icd10_codes = models.ManyToManyField(Diagnosis)
    medications = models.ManyToManyField(Medication)
    remarks = models.TextField(blank=True)
    is_latest = models.BooleanField(default=False)

class MedicalHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='medical_histories')
    description = models.TextField()
    date = models.DateField()

class Report(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reports')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    report_code = models.CharField(max_length=20, blank=True)

def create_sample_data():
    # Create sample doctors
    dr_burak = Doctor.objects.create(name='Mehmet Burak', diploma_no='25944/29412', branch='Genel Cerrahi')
    dr_ayse = Doctor.objects.create(name='Ayşe Yılmaz', diploma_no='12185', branch='Dahiliye')

    # Create sample profiles
    p1 = Profile.objects.create(
        first_name='Ayşe', last_name='Yılmaz', tc_no='15746029352', birth_date='1980-05-12', gender='Kadın', address='İstanbul')
    p2 = Profile.objects.create(
        first_name='Mehmet', last_name='Burak', tc_no='15746029353', birth_date='1975-09-23', gender='Erkek', address='Ankara')

    # Diagnoses (ICD-10)
    d1 = Diagnosis.objects.create(code='A09', description='Gastroenterit')
    d2 = Diagnosis.objects.create(code='B35', description='Mantar enfeksiyonu')
    d3 = Diagnosis.objects.create(code='I10', description='Hipertansiyon')

    # Medications
    m1 = Medication.objects.create(name='CIPRO 500 MG.14 TB.', barcode='8699578090425', dosage='1', period='Günde', amount=2, unit='TB')
    m2 = Medication.objects.create(name='TRAVAZOL %1 + %0,1 KREM (15 G)', barcode='8699569350040', dosage='1', period='Günde', amount=3, unit='KREM')
    m3 = Medication.objects.create(name='RAMIPRIL 5 MG', barcode='8699512345678', dosage='1', period='Günde', amount=1, unit='TB')

    # Medical histories
    MedicalHistory.objects.create(profile=p1, description='Gastroenterit', date='2025-07-10')
    MedicalHistory.objects.create(profile=p1, description='Mantar enfeksiyonu', date='2025-07-12')
    MedicalHistory.objects.create(profile=p2, description='Hipertansiyon', date='2025-06-15')

    # Reports
    Report.objects.create(profile=p1, title='Genel Cerrahi Raporu', content='Ameliyat sonrası kontrol.', date='2025-07-13', report_code='RPT001')
    Report.objects.create(profile=p2, title='Dahiliye Raporu', content='Düzenli ilaç kullanımı önerildi.', date='2025-07-14', report_code='RPT002')

    # Prescriptions
    presc1 = Prescription.objects.create(
        profile=p1,
        doctor=dr_burak,
        date='2025-07-13',
        protocol_no='26404592',
        provision_type='Normal',
        prescription_type='Normal',
        prescription_subtype='Ayaktan',
        remarks='Seri dağıtım reçete',
        is_latest=True
    )
    presc1.icd10_codes.add(d1)
    presc1.medications.add(m1, m2)

    presc2 = Prescription.objects.create(
        profile=p1,
        doctor=dr_ayse,
        date='2025-06-20',
        protocol_no='26404593',
        provision_type='Normal',
        prescription_type='Normal',
        prescription_subtype='Ayaktan',
        remarks='Önceki reçete',
        is_latest=False
    )
    presc2.icd10_codes.add(d2)
    presc2.medications.add(m2)

    presc3 = Prescription.objects.create(
        profile=p2,
        doctor=dr_burak,
        date='2025-07-14',
        protocol_no='26404594',
        provision_type='Normal',
        prescription_type='Normal',
        prescription_subtype='Ayaktan',
        remarks='Son reçete',
        is_latest=True
    )
    presc3.icd10_codes.add(d3)
    presc3.medications.add(m3)

