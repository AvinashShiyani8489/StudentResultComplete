# Generated by Django 3.2.6 on 2021-09-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppResult', '0008_teachermodel_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='studentresultmodel',
            unique_together=set(),
        ),
    ]
