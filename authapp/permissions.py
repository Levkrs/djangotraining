from django.http import Http404


PERMISSION_DENIED_MESSAGE = 'У вас нет прав просматривать эту страницу'

class ApplicantPermissionMixin:
    """Класс выделения прав доступа на основе роли для соискателя"""
    def has_permission(self):
        return self.request.user.role == 'REC' or self.request.user.role == 'MOD'

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404 # TODO заменить на 403 или своим шаблоном отказа в доступе
        return super().dispatch(request, *args, **kwargs)

class CompanyPermissionMixin(ApplicantPermissionMixin):
    """Класс выделения прав доступа на основе роли для работодателя"""
    def has_permission(self):
        return self.request.user.role == 'HR' or self.request.user.role == 'MOD'

class ModeratorPermissionMixin:
    """Класс выделения прав доступа на основе роли для модератора"""
    def has_permission(self):
        return self.request.user.role == 'MOD'