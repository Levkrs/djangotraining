from django.db import models


class News(models.Model):
    """
    News
    """

    class Meta:
        get_latest_by = '-created_at'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок новости')
    body = models.TextField(blank=False, null=False, verbose_name='Текст новости')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
