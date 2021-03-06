# Generated by Django 3.2.6 on 2021-09-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppResult', '0004_studentresultmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentresultmodel',
            old_name='student_first_name',
            new_name='student_name',
        ),
        migrations.RemoveField(
            model_name='studentresultmodel',
            name='admission_std',
        ),
        migrations.RemoveField(
            model_name='studentresultmodel',
            name='admission_stream',
        ),
        migrations.RemoveField(
            model_name='studentresultmodel',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='studentresultmodel',
            name='student_last_name',
        ),
        migrations.RemoveField(
            model_name='studentresultmodel',
            name='subject_name',
        ),
        migrations.RemoveField(
            model_name='studentresultmodel',
            name='teacher_id',
        ),
        migrations.AlterField(
            model_name='studentresultmodel',
            name='percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='studentresultmodel',
            name='total_marks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='join_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='leave_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='teacher_id',
            field=models.CharField(db_index=True, max_length=50, primary_key=True, serialize=False),
        ),
    ]
