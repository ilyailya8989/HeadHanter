from django import forms
from .models import Resume, Vacancy

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'