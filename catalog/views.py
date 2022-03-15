from django.shortcuts import render, get_object_or_404
import datetime
from .models import Patient, Case, Visit, Service, Diagnosis, Schedule, UserLastName
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .forms import RegisterPatientForm

class UserCaseListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = Case
    # template_name ='catalog/case_list.html'
    # paginate_by = 10

    def get_queryset(self):
        return Case.objects.filter(doctor__exact=self.request.user)

    # filter(doctor=self.request.user).order_by('date')
@login_required
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    us = User.objects.get(username=request.user)
    num_patients=Patient.objects.filter(case__doctor__exact=request.user).count()
    num_cases=Case.objects.all().count()
    num_cases_leo=Case.objects.filter(doctor__exact=request.user).count()
    # num_visits=Visit.objects.count()  # Метод 'all()' применён по умолчанию.
    num_services = Service.objects.count()
    current_date = datetime.date.today()
    # print(request.session.keys())
    num_visits = request.session.get('num_visits', 0)
    request.session.update({'num_visits': num_visits+1})
    num_visits = request.session.get('num_visits')
    # request.session.modified = True
    # request.session['num_visits'] += 1
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context

    return render(
            request,
            'index.html',
            context={'num_patients':num_patients,'num_cases':num_cases,
                    'num_cases_leo':num_cases_leo,'num_visits':num_visits,'num_services':num_services,
                    'current_date':current_date, 'us':us})
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class PatientListView(generic.ListView):
    model = Patient

    def get_queryset(self):
        return Patient.objects.filter(case__doctor__exact=self.request.user)

class DiagnosisListView(generic.ListView):
    model = Diagnosis
    paginate_by = 20

    def get_queryset(self):
        return Diagnosis.objects.all()

class ScheduleListView(generic.ListView):
    model = Schedule
    paginate_by = 20

    def get_queryset(self):
        return Schedule.objects.all() #

class PatientDetailView(generic.DetailView):
    model = Patient


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
            qs = qs.filter(services__istartswith=self.q)

        return qs

@permission_required('catalog.can_edit')
def change_patient(request,pk):
    patient = get_object_or_404(Patient, pk=pk)

    # Если данный запрос типа POST, тогда
    if request.method == 'POST':

        # Создаём экземпляр формы и заполняем данными из запроса (связывание, binding):
        form = RegisterPatientForm(request.POST)

        # Проверка валидности данных формы:
        if form.is_valid():
            # Обработка данных из form.cleaned_data
            #(здесь мы просто присваиваем их полю due_back)
            print(patient)
            patient.save()

            # Переход по адресу 'all-borrowed':
            return HttpResponseRedirect(reverse('catalog:patient-detail', args=[patient.id]))

    # Если это GET (или какой-либо ещё), создать форму по умолчанию.
    else:
        date = datetime.date.today()
        form = RegisterPatientForm(initial={'date': date,})

    return render(request, 'catalog/change_patient.html', {'form': form, 'patient':patient})

class PatientCreate(CreateView):
    model = Patient
    fields = '__all__'
    exclude = ['id',]
    initial={'date':'12/10/2016',}

class PatientUpdate(UpdateView):
    model = Patient
    fields = '__all__'
    exclude = ['id', ]

# a = 1_000_000

class PatientDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('patients')