# Generated by Django 4.2.7 on 2023-11-30 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='detailed_description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Подробное описание'),
        ),
    ]
