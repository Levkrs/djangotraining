from django.contrib import admin

from .models import Company, Job


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Поля таблицы Компания в админке
    """
    list_display = ('id', 'name', 'location', 'link', 'is_active',
                    'created_at', 'updated_at',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """
    Поля таблицы Вакансии в админке
    """
    list_display = ('id', 'is_active', 'created_at', 'updated_at',)
