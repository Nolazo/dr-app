# from .views import (ListPatientsView, DetailPatientView,     ListInsuranceView,
#     DetailInsuranceView,
#     ListMedicalRecordView,
#     DetailMedicalRecordView,
# )

# urlpatterns = [
#     path('patients/', ListPatientsView.as_view()),
#     path('patients/<int:pk>/', DetailPatientView.as_view()),
#     path('insurances/', ListInsuranceView.as_view()),
#     path('insurances/<int:pk>/', DetailInsuranceView.as_view()),
#     path('medicalrecords/', ListMedicalRecordView.as_view()),
#     path('medicalrecords/<int:pk>/', DetailMedicalRecordView.as_view()),
# ]
from django.urls import path
from .views import get_patients

from rest_framework.routers import DefaultRouter
from .viewsets import PatientViewSet, InsuranceViewSet, MedicalRecordViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('insurances', InsuranceViewSet)
router.register('medicalrecords', MedicalRecordViewSet)
#router.register(r'a', get_patients, basename='patient')

urlpatterns =[
    path('', get_patients, name='get_patients'),
    #path('add/', PatientFormView.as_view(), name='add_patient'),
] + router.urls
