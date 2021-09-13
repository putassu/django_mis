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
    id = models.UUIDField(primary_key=True,default=uuid.uuid4(), help_text="ID пациента")
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
        return '%s (%s %s)' % (self.id,self.first_name,self.last_name)


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('Перейти к пациенту', args=[str(self.id)])

class Case(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4(), help_text="ID случая")
    id_p = models.ForeignKey('Patient',on_delete=models.SET_NULL, null=True)
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
    diagnosis = models.ForeignKey('Diagnosis', on_delete=models.SET_NULL, null=True, help_text="Выберите диагноз")
    # character = 
    # diagnosis = 
    class Meta:
        ordering = ["date"]
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
        return '%s (%s) ' % (self.date,self.id_p.first_name)

class Visit(models.Model):
    """
    Model representing an author.
    """
    id = models.UUIDField(primary_key=True,default=uuid.uuid4(),help_text="ID посещения")
    id_c = models.ForeignKey('Case',on_delete=models.SET_NULL, null=True)
    date = models.DateField(("Дата посещения"), default=datetime.date.today)
    # help_type = 
    # visit_type = 
    # place = 
    class Meta:
        ordering = ["date"]
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
        return '%s, %s' % (self.id, self.date)

class Diagnosis(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    code = models.CharField(primary_key=True,max_length=20, help_text="Код болезни")
    name = models.CharField(max_length=200, help_text="Название болезни")
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s, %s' % (self.code, self.name)

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
#         d = Diagnosis(name=name_,code=code_)
#         d.save()