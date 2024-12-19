from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer
from .models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    @action(['POST'], detail=True, url_path='set-on-vacation')
    def set_on_vacation(self, requests, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status": "El doctor estÃ¡ en vacaciones"})

    @action(['POST'], detail=True, url_path='set-off-vacation')
    def set_off_vacation(self, requests, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status": "El doctor NO estÃ¡ en vacaciones"})


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

class MedicalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()