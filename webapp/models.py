from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    description = models.CharField(max_length=50, verbose_name="Описание")
    status = models.CharField(max_length=20, default='Новая', verbose_name="Статус", choices=status_choices)
    due_date = models.DateField(verbose_name='Дата выполнения', null=True, blank=True)
    detailed_description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Подробное описание')

    def get_display_status(self):
        dict_status_choices = dict(status_choices)
        return dict_status_choices.get(self.status)

    def __str__(self):
        return f'{self.id}. {self.description} {self.due_date} {self.status}'


