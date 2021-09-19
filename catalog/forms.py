from dal import autocomplete

from django import forms
from catalog.models import Diagnosis, Case, Visit, Service


class Form(forms.ModelForm):
    diagnosis = forms.ModelChoiceField(
        queryset=Diagnosis.objects.all(),
        widget=autocomplete.ModelSelect2(url='diagnosis-autocomplete')
    )

    class Meta:
        model = Case
        fields = ('__all__')

class Form2(forms.ModelForm):
    services = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        widget=autocomplete.ModelSelect2(url='services-autocomplete')
    )

    class Meta:
        model = Visit
        fields = ('__all__')