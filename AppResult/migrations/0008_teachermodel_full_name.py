# Generated by Django 3.2.6 on 2021-09-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppResult', '0007_auto_20210928_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermodel',
            name='full_name',
            field=models.CharField(default='avinash', max_length=50),
            preserve_default=False,
        ),
    ]