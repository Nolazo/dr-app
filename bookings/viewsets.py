from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import AppointmentSerializer, MedicalNoteSerializer
from .models import Appointment, MedicalNote


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    List all appointments or create a new appointment.
    """
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class MedicalNoteViewSet(viewsets.ModelViewSet):
    """
    List all medical notes or create a new medical note.
    """
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()