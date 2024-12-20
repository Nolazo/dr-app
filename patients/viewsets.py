from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord


class PatientViewSet(viewsets.ModelViewSet):
    """
    List all patients or create a new patient.
    """
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class InsuranceViewSet(viewsets.ModelViewSet):
    """
    List all insurances or create a new insurance.
    """
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()
    

class MedicalRecordViewSet(viewsets.ModelViewSet):
    """
    List all medical records or create a new medical record.
    """
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()