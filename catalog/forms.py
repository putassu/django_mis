from dal import autocomplete

from django import forms
from catalog.models import Case,Diagnosis

class Form(forms.ModelForm):
    diagnosis = forms.ModelChoiceField(
        queryset=Diagnosis.objects.all(),
        widget=autocomplete.ModelSelect2(url='country-autocomplete')
    )

    class Meta:
        model = Case
        fields = ('__all__')