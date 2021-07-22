from django.db import models


class Widget(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    configurations = models.JSONField(verbose_name='Конфигурация', default=dict)

    class Meta:
        verbose_name = 'Виджет'
        verbose_name_plural = 'Виджеты'

    def __str__(self):
        return '{0}:{1}'.format(self.id, self.title)


class Site(models.Model):
    domain = models.CharField(max_length=200, verbose_name='Домен сайта')
    widgets = models.ManyToManyField(Widget, verbose_name='Виджеты', blank=True)

    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'

    def __str__(self):
        return '{0}:{1}'.format(self.id, self.domain)


class Brand(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    sites = models.ManyToManyField(Site, verbose_name='Сайты', blank=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return '{0}:{1}'.format(self.id, self.title)
