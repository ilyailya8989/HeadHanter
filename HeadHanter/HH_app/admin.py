from django.contrib import admin

from HH_app.models import Resume, Vacancy, Company_name

# Register your models here.
admin.site.register(Resume)
admin.site.register(Vacancy)
admin.site.register(Company_name)