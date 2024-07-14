from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Vacancy, Resume
from .forms import VacancyForm, ResumeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Вакансии
class VacancyListView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        return render(request, 'HH_app/vacancy_list.html', {'vacancies': vacancies})

class VacancyDetailView(View):
    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        return render(request, 'HH_app/vacancy_detail.html', {'vacancy': vacancy})

@method_decorator(login_required, name='dispatch')
class VacancyCreateView(View):
    def get(self, request):
        form = VacancyForm()
        return render(request, 'HH_app/vacancy_form.html', {'form': form})

    def post(self, request):
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
        return render(request, 'HH_app/vacancy_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class VacancyUpdateView(View):
    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        form = VacancyForm(instance=vacancy)
        return render(request, 'HH_app/vacancy_form.html', {'form': form})

    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
        return render(request, 'HH_app/vacancy_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class VacancyDeleteView(View):
    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        return render(request, 'HH_app/vacancy_confirm_delete.html', {'vacancy': vacancy})

    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        vacancy.delete()
        return redirect('vacancy_list')

# Резюме
class ResumeListView(View):
    def get(self, request):
        resumes = Resume.objects.all()
        return render(request, 'HH_app/resume_list.html', {'resumes': resumes})

class ResumeDetailView(View):
    def get(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk)
        return render(request, 'HH_app/resume_detail.html', {'resume': resume})

@method_decorator(login_required, name='dispatch')
class ResumeCreateView(View):
    def get(self, request):
        form = ResumeForm()
        return render(request, 'HH_app/resume_form.html', {'form': form})

    def post(self, request):
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
        return render(request, 'HH_app/resume_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ResumeUpdateView(View):
    def get(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk)
        form = ResumeForm(instance=resume)
        return render(request, 'HH_app/resume_form.html', {'form': form})

    def post(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk)
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
        return render(request, 'HH_app/resume_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ResumeDeleteView(View):
    def get(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk)
        return render(request, 'HH_app/resume_confirm_delete.html', {'resume': resume})

    def post(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk)
        resume.delete()
        return redirect('resume_list')
