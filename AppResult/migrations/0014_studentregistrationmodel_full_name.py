# Generated by Django 3.2.6 on 2021-09-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppResult', '0013_auto_20210929_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistrationmodel',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
