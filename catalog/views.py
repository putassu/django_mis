from django.shortcuts import render

from .models import Patient, Case, Visit

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_patients=Patient.objects.all().count()
    num_cases=Case.objects.all().count()
    num_cases_leo=Case.objects.filter(Patient__first_name__iexact='лев').count()
    num_visits=Visit.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_patients':num_patients,'num_cases':num_cases,'num_cases_leo':num_cases_leo,'num_visits':num_visits},
    )
from dal import autocomplete
from catalog.models import Diagnosis, Service

class DiagnosisAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Diagnosis.objects.none()

        qs = Diagnosis.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
# Create your views here.
class ServicesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Service.objects.none()

        qs = Service.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs