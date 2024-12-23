from django.shortcuts import render
from django.views import generic

from .forms import DoctorForm
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer


def get_doctors(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    serializer_date = serializer.data
    return render(request, 'doctors/doctors.html', {'doctors': serializer_date})


class DoctorFormView(generic.FormView):
    form_class = DoctorForm
    template_name = 'doctors/add_doctor.html'
    success_url = '/doctors/list/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
