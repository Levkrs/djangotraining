from django.contrib import admin

from applicantapp.models import Resume, Education, Experience

admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Experience)