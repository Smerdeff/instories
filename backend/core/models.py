from django.db import models

class Option(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название опции", unique=True)
    value = models.BooleanField(verbose_name='Значение')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Опция'
        verbose_name_plural='Опции'

class Pushes(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок уведомления', )
    text = models.TextField(verbose_name='Текст уведомлния', )
    created_at = models.DateTimeField(auto_now_add=True, editable=False, )
    sent_at = models.DateField(verbose_name='Дата отправки')
    is_sent = models.BooleanField(verbose_name='Отправлен', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Пуш уведомление'
        verbose_name_plural='Пуш уведомления'

