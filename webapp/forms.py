from django import forms
from django.forms import widgets
from webapp.models import status_choices


class TaskForm(forms.Form):
    description = forms.CharField(max_length=50, required=True, label='Описание')
    status = forms.ChoiceField(choices=status_choices, required=True, label='Статус')
    due_date = forms.DateField(label='Дата выполнения', required= False)
    detailed_description = forms.CharField(max_length=1000, required=False, widget=widgets.Textarea,
                                           label='Подробное описание')