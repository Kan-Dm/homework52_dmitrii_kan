from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    description = models.CharField(max_length=50, verbose_name="Описание")
    status = models.CharField(max_length=10, default='Новая', verbose_name="Статус", choices=status_choices)
    due_date = models.DateField(verbose_name='Дата выполнения', null=True, blank=True)

    def __str__(self):
        return f'{self.id}. {self.description}'
