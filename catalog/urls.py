from django.urls import path, re_path, include
from django.conf.urls import url


from catalog.views import DiagnosisAutocomplete, ServicesAutocomplete,\
    index, PatientListView, PatientDetailView, DiagnosisListView, UserCaseListView, ScheduleListView, change_patient

app_name = 'catalog'
urlpatterns = [
    url(
        'diagnosis-autocomplete/',
        DiagnosisAutocomplete.as_view(),
        name='diagnosis-autocomplete',
    ),
    url(
        r'^services-autocomplete/$',
        ServicesAutocomplete.as_view(),
        name='services-autocomplete',
    ),
]
urlpatterns+=[
    path('', index, name='index'),]
urlpatterns+=[path('patients/', PatientListView.as_view(), name='patients'),]
urlpatterns+=[path('patient/<int:pk>', PatientDetailView.as_view(), name='patient-detail'),]
urlpatterns+=[path('diagnosis/', DiagnosisListView.as_view(), name='diagnosis'),]
urlpatterns+=[path('cases/', UserCaseListView.as_view(), name='cases'),]
urlpatterns+=[path('schedule/', ScheduleListView .as_view(), name='schedule'),]
urlpatterns+=[path('patient/<int:pk>/change_patient/', change_patient, name='change_patient'),]
