# Generated by Django 3.2.13 on 2022-05-28 15:29

from django.db import migrations
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0056_auto_20211106_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='important_notes',
            field=django_bleach.models.BleachField(blank=True, help_text='This text is directly shown on the registration page, so that helpers cannot\n                    miss notes in the description.', verbose_name='Important notes'),
        ),
        migrations.AddField(
            model_name='job',
            name='important_notes_de',
            field=django_bleach.models.BleachField(blank=True, help_text='This text is directly shown on the registration page, so that helpers cannot\n                    miss notes in the description.', null=True, verbose_name='Important notes'),
        ),
        migrations.AddField(
            model_name='job',
            name='important_notes_en',
            field=django_bleach.models.BleachField(blank=True, help_text='This text is directly shown on the registration page, so that helpers cannot\n                    miss notes in the description.', null=True, verbose_name='Important notes'),
        ),
    ]
