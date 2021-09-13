from django.urls import path
from django.conf.urls import url


from catalog.views import DiagnosisAutocomplete

urlpatterns = [
    url(
        r'^country-autocomplete/$',
        DiagnosisAutocomplete.as_view(),
        name='country-autocomplete',
    ),
]