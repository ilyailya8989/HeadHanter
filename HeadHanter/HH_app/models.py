from django.contrib.auth.models import User
from django.db import models

#нужны для проверки
from django.core.exceptions import ValidationError
import datetime


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()
    birth_date = models.DateField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()

    def __str__(self):
        return f' Имя {self.name}'


    def valid(self):
        if "spam" in self.email.lower():
            raise ValidationError("Email не должен содержать слово 'spam'.")

        if self.birth_date > datetime.date.today(): #бепрет сегодняшнюю дату
            raise ValidationError("Дата рождения не может быть в будущем.")
        super().valid()

class Company_name(models.Model):
    name = models.CharField(max_length=55)
    def __str__(self):
        return f'company {self.name}'

class Vacancy(models.Model):
    job_title = models.CharField(max_length=55) #Название вакансии
    company_name = models.ForeignKey(Company_name, on_delete=models.CASCADE) #Название компании

    salary = models.IntegerField(default=0)
    required_skills = models.TextField()
    responsibilities = models.TextField() #Обязанности
    adress = models.TextField()

    def __str__(self):
        return f'вакансия {self.job_title}'


