from django.urls import path
from .views import get_doctors, DoctorFormView

from rest_framework.routers import DefaultRouter
from .viewsets import (DoctorViewSet, DepartmentViewSet,
                       DoctorAvailabilityViewSet, MedicalNoteViewSet)


router = DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('departments', DepartmentViewSet)
router.register('doctoravailabilities', DoctorAvailabilityViewSet)
router.register('medicalnotes', MedicalNoteViewSet)

urlpatterns = [
    path('list/', get_doctors, name='get_doctors'),
    path('add/', DoctorFormView.as_view(), name='add_doctor'),
] + router.urls