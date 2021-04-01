from django.http import Http404

# Свои классы для предоставления прав на основе роли юзера
# пока не используются

PERMISSION_DENIED_MESSAGE = 'У вас нет прав просматривать эту страницу'

class ApplicantPermissionMixin:
    """Класс проверки прав доступа на основе роли для соискателя"""
    def has_permission(self):
        return self.request.user.role == 'REC'

    def dispatch(self, request, *args, **kwargs):
        if self.has_permission():
            raise Http404
        return super().dispatch(request, *args, **kwargs)

class CompanyPermissionMixin(ApplicantPermissionMixin):
    """Класс проверки прав доступа на основе роли для работодателя"""
    def has_permission(self):
        return self.request.user.role == 'HR'

class ModeratorPermissionMixin:
    """Класс проверки прав доступа на основе роли для модератора"""
    def has_permission(self):
        return self.request.user.role == 'MOD'