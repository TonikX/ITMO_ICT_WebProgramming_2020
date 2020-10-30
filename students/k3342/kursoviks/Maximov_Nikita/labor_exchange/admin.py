from django.contrib import admin
from .models import Education, Profession, Field, Applicant, Resume, Course, CourseCertificate, Gratuity, Employer, Vacancy, Application

admin.site.register(Employer)
admin.site.register(Education)
admin.site.register(Profession)
admin.site.register(Applicant)
admin.site.register(Application)
admin.site.register(Resume)
admin.site.register(Course)
admin.site.register(CourseCertificate)
admin.site.register(Gratuity)
admin.site.register(Vacancy)
admin.site.register(Field)
