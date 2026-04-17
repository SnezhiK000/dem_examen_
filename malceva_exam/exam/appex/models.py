from django.db import models
from django.utils import timezone

#Роли пользователей
class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)

#Компании в которых работает пользователь
class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    inn = models.CharField( max_length= 12)
    legal_address = models.CharField(max_length=500)
    phone = models.CharField(max_length=35)

#Должность
class Position(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)

#Серия паспорта
class PassportSeries(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=4)

#Пользоатели
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_fio = models.CharField(max_length=250)
    login = models.CharField(max_length=250)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    password = models.CharField(max_length=250)
    passport_series = models.ForeignKey(PassportSeries, on_delete=models.CASCADE, null=True)
    passport_number = models.CharField(max_length=6)
    address = models.CharField(max_length=600)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    last_login = models.DateTimeField(null=True, blank=True)
