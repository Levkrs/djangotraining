from django.contrib import admin

from .models import Company, Job


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Поля таблицы Компания в админке
    """
    list_display = ('id', 'name', 'status', 'location', 'link',
                    'created_at', 'updated_at', 'views_count',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """
    Поля таблицы Вакансии в админке
    """
    list_display = ('id', 'status', 'grade', 'category', 'salary', 'city', 'employment',
                    'work_schedule', 'experience', 'created_at', 'updated_at', 'views_count',)
