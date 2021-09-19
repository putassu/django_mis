from django.urls import path
from django.conf.urls import url


from catalog.views import DiagnosisAutocomplete, ServicesAutocomplete

urlpatterns = [
    url(
        r'^diagnosis-autocomplete/$',
        DiagnosisAutocomplete.as_view(),
        name='diagnosis-autocomplete',
    ),
    url(
        r'^services-autocomplete/$',
        ServicesAutocomplete.as_view(),
        name='services-autocomplete',
    ),
]