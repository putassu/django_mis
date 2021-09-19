from django.db import models
from django.urls import reverse
import uuid
import datetime
from django.utils.html import format_html
from django import forms
# Create your models here.
def get_smo():
    f = open('C:/Users/Leo/django_mis/catalog/reestSMO.csv', 'r', encoding = 'utf-8')
    content = f.readlines()
    SMO_ = []
    for line in content:
        li = line.split(';')
        c = (li[1],li[5])
        SMO_.append(c)
    f.close()
    SMO = SMO_[1:]
    return SMO
class Patient(models.Model):
    """
    Model representing a patient
    """
    id = models.AutoField(primary_key=True,help_text="ID пациента")
    first_name = models.CharField("Имя",max_length=25)
    last_name = models.CharField("Фамилия",max_length=25)
    patronym = models.CharField("Отчество",max_length=25,blank=True)
    SEX = (
        ('1', 'Мужской'),
        ('2', 'Женский'),
        ('3', 'Не определен'),
    )
    sex = models.CharField("Пол",max_length=1, choices=SEX, blank=True, help_text='Выберите пол')

    DISABILITY= (
        ('1', '1 группа'),
        ('2', '2 группа'),
        ('3', '3 группа'),
        ('4', 'ребенок-инвалид'),
    )

    disability = models.CharField("Инвалидность",max_length=1, choices=DISABILITY, blank=True, help_text='Группа инвалидности')
    SMO__ = get_smo()
    smo = models.CharField("СМО",max_length=50, choices=SMO__, blank=True, help_text='Страховая медицинская организация')
    oms = models.CharField('ОМС',max_length=20, help_text='Номер ОМС')
    date = models.DateField(("Дата рождения"), default=datetime.date.today)
    class Meta:
        ordering = ["last_name"]
        verbose_name_plural = 'Пациенты'
        verbose_name = 'пациента'
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s %s (%s) г.р.' % (self.first_name,self.last_name, self.date)


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('Перейти к пациенту', args=[str(self.id)])

class Case(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """

    id = models.AutoField(primary_key=True, help_text="ID случая")
    id_p = models.ForeignKey('Patient',verbose_name="ID пациента",on_delete=models.SET_NULL, null=True)
    date = models.DateField(("Дата открытия"), default=datetime.date.today)
    REASONS = [
        ('1', 'Лечебно-диагностический прием '),
        ('2', 'Консультативный прием '),
        ('3', 'Диспансерное наблюдение '),
        ('4', 'Профилактический прием'),
        ('5', 'Профессиональный осмотр'),
        ('6', 'Реабилитационный прием'),
        ('7', 'Зубопротезный прием'),
        ('8', 'Протезно-ортопедический прием'),
        ('9', 'Обращение в центр здоровья'),
        ('10', 'Дополнительная диспансеризация'),
        ('11', 'Патронаж'),
        ('12', 'Другие'),
    ]

    reason = models.CharField('Повод обращения',max_length=2, choices=REASONS, blank=True, help_text='Повод обращения')

    RESULTS = [
        ('5', 'Здоров'),
        ('1', 'Выздоровление'),
        ('3', 'Без изменений'),
        ('2', 'Улучшение'),
        ('4', 'Ухудшение'),
        ('6', 'Летальный исход'),
    ]
    result = models.CharField('Результат',max_length=2, choices=RESULTS, blank=True, help_text='Исход случая')
    diagnosis = models.ForeignKey('Diagnosis',verbose_name="Диагноз", on_delete=models.SET_NULL, null=True, help_text="Выберите диагноз")
    CHARACTER = [
        ('1', 'Впервые в жизни установленное хроническое'),
        ('2', 'Ранее установленное хроническое'),
        ('3', 'Острое'),
    ]
    character = models.CharField('Характер заболевания', max_length=2, choices=CHARACTER, blank=True,
                                 help_text='Характер заболевания')
    # diagnosis =
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = 'Случаи'
        verbose_name = 'случай'
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('Перейти к случаю', args=[str(self.id)])
    def __str__(self):
        """
        String for representing the Model object
        """
        try:
            fn = self.id_p.first_name
        except:
            fn = 'Здесь ничего нет'
        return '%s (%s) ' % (self.date,fn)

class Visit(models.Model):
    """
    Model representing an author.
    """
    id = models.AutoField(primary_key=True,help_text="ID посещения")
    id_c = models.ForeignKey('Case',verbose_name="ID случая",on_delete=models.SET_NULL, null=True)
    services = models.ForeignKey('Service',verbose_name="Услуга",on_delete=models.SET_NULL, null=True)
    date = models.DateField(("Дата посещения"), default=datetime.date.today)
    HELPTYPE = [('10', 'Первичная медико-санитарная помощь'),
                ('1', 'Первичная доврачебная медико-санитарная помощь'),
                ('2', 'Первичная врачебная медико-санитарная помощь'),
                ('3', 'Первичная специализированная медико-санитарная помощь'),
                ('4', 'Специализированная медицинская помощь'),
                ('8', 'Высокотехнологичная специализированная медицинская помощь'),
                ('6', 'Паллиативная медицинская помощь'),
                ('5', 'Скорая медицинская помощь'),
                ('7', 'Иные'),
                ]
    help_type = models.CharField('Вид оказываемой помощи', max_length=2, choices=HELPTYPE, blank=True,
                                 help_text='Вид оказываемой помощи')
    # visit_type = 
    # place = 
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = 'Посещения'
        verbose_name = 'посещение'
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('Посещение', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.services, self.date)

class Diagnosis(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    code = models.CharField(primary_key=True,verbose_name='Код болезни(МКБ-10)',max_length=20, help_text="Код болезни")
    name = models.CharField(max_length=200,verbose_name='Название болезни(МКБ-10)', help_text="Название болезни")

    class Meta:
        ordering = ["-name"]
        verbose_name_plural = 'Диагнозы'
        verbose_name = 'Диагноз'
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s, %s' % (self.code, self.name)

class Service(models.Model):
    """
    Model representing an author.
    """
    id = models.CharField(max_length=20,verbose_name="Код услуги",primary_key=True,help_text="Код услуги")
    # id_v = models.ForeignKey('Visit',verbose_name="ID посещения",on_delete=models.SET_NULL, null=True)
    # date = models.ForeignKey('Visit', default=datetime.date.today)
    services = models.CharField(verbose_name="Название услуги",max_length=200, help_text="Название услуги")
    class Meta:
        # ordering = ["-date"]
        verbose_name_plural = 'Услуги'
        verbose_name = 'услугу'
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('Услуга', args=[str(self.services)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s - %s' % (self.id, self.services)

PATIENTS = [tuple((str(pat), (str(pat)))) for pat in list(Patient.objects.all())]
PATIENTS.append(tuple(('Нет записи', 'Нет записи')))
print(PATIENTS)

class Schedule(models.Model):
    """
    Model representing an author.
    """
    PATIENTS = [tuple((str(pat), (str(pat)))) for pat in list(Patient.objects.all())]
    PATIENTS.append(tuple(('Нет записи', 'Нет записи')))
    date = models.DateField(("Дата посещения"),primary_key=True, default=datetime.date.today)
    id_10_00 = models.CharField(max_length=50,choices=PATIENTS,verbose_name="10:00", null=True, default='Нет записи')
    id_10_20 = models.CharField(max_length=50,choices=PATIENTS, verbose_name="10:20", null=True, default='Нет записи')
    id_10_40 = models.CharField(max_length=50, choices=PATIENTS, verbose_name="10:40", null=True, default='Нет записи')
    id_11_00= models.CharField(max_length=50, choices=PATIENTS, verbose_name="11:00", null=True, default='Нет записи')
    id_11_20 = models.CharField(max_length=50, choices=PATIENTS, verbose_name="11:20", null=True, default='Нет записи')
    id_11_40 = models.CharField(max_length=50, choices=PATIENTS, verbose_name="11:40", null=True, default='Нет записи')
    id_13_00 = models.CharField(max_length=50, choices=PATIENTS, verbose_name="13:00", null=True, default='Нет записи')
    id_13_20 = models.CharField(max_length=50, choices=PATIENTS, verbose_name="13:20", null=True, default='Нет записи')
    id_13_40 = models.CharField(max_length=50, choices=PATIENTS, verbose_name="13:40", null=True, default='Нет записи')
    id_14_00 = models.CharField(max_length=50, choices=PATIENTS, verbose_name="14:00", null=True, default='Нет записи')
    id_14_20 = models.CharField(max_length=50, choices=PATIENTS, verbose_name="14:20", null=True, default='Нет записи')
    id_14_40 = models.CharField(max_length=50, choices=PATIENTS, verbose_name="14:40", null=True, default='Нет записи')

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = 'Смены'
        verbose_name = 'Смену'
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('Смены', args=[str(self.date)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s %s %s %s %s %s %s %s %s %s %s' % (self.date, self.id_10_00, self.id_10_20, self.id_10_40,
                                               self.id_11_00, self.id_11_20, self.id_11_40, self.id_13_00,
                                               self.id_13_20, self.id_13_40, self.id_14_00)


# with open('C:/Users/Leo/django_mis/catalog/diagnosis.csv', 'r', encoding='utf-8') as f:
#     content = f.readlines()
#     i=0
#     for line in content:
#         i+=1
#         if i < 3:
#             continue
#         lines = line.split(';')
#         name_ = lines[1].strip('"""')
#         code_ = lines[2]
#         print('извлёк ', code_, name_)
#         d = Diagnosis(name=name_,code=code_)
#         d.save()
#with open('C:/Users/Leo/django_mis/catalog/services.csv', 'r', encoding='utf-8') as f:
    # content = f.readlines()
    # i=0
    # for line in content:
    #     i+=1
    #     if i < 3:
    #         continue
    #     lines = line.split(';')
    #     name_ = lines[2].strip("'")
    #     code_ = lines[1].strip("'")
    #     s = Service(id=code_, service=name_)
    #     s.save()
