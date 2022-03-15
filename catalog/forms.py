from dal import autocomplete
from catalog.models import Diagnosis, Case, Visit, Service, \
    Patient
from django import forms
from django.core.exceptions import ValidationError
import datetime

class Form(forms.ModelForm):
    diagnosis = forms.ModelChoiceField(
        queryset=Diagnosis.objects.all(),
        widget=autocomplete.ModelSelect2(url='catalog:diagnosis-autocomplete')
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


class RegisterPatientForm(forms.ModelForm):
    # date = forms.DateField(help_text="Дата рождения")

    def clean_date(self):
        data = self.cleaned_data['date']

        if data < datetime.date(1910,5,5):
            raise ValidationError("Пациенту не может быть больше 110 лет!")
        if data > datetime.date.today():
            raise ValidationError("Пациент не может родиться в будущем!")
        return data

    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['id',]
        labels = {'date': 'Дата рождения', 'first_name': 'Имя', 'last_name': 'Фамилия', 'smo': 'Страховая организация',
                  'oms': 'Полис ОМС', 'sex': 'Пол', 'disability': 'Инвалидность',}