from django.shortcuts import render
from django.views import generic

#from .forms import PatientForm
from .models import Patient, Insurance, MedicalRecord
from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer


def get_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    serializer_date = serializer.data
    return render(request, 'patients/patients.html', {'patients': serializer_date})