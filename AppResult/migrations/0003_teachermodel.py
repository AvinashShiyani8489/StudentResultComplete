# Generated by Django 3.2.6 on 2021-09-27 07:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppResult', '0002_auto_20210927_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('teacher_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_firstName', message='First Name must be Alphabet', regex='^[a-zA-Z]*$')])),
                ('last_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_firstName', message='First Name must be Alphabet', regex='^[a-zA-Z]*$')])),
                ('gender', models.CharField(choices=[(None, 'Choose your gender'), ('male', 'Male'), ('female', 'Female'), ('prefer not to say', 'prefer not to say')], default=None, max_length=50)),
                ('birth_date', models.DateField()),
                ('mobile', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(code='Invalid_MobileNumber', message='Only Numberic or start with + ', regex='^[0-9+]*$')])),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_Email', message='Email must be properly(user@domanname.com or in or edu)', regex='^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$')])),
                ('address', models.TextField()),
                ('area', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='Invalid City Name', message='City Name must be Alphabet', regex='^[a-zA-Z]*$')])),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(code='Invalid Pincode', message='Only Numberic', regex='^[0-9]*$')])),
                ('subject_name', models.CharField(choices=[(None, 'Choose Student Stream'), ('Science', 'Science'), ('Math', 'Maths'), ('English', 'English'), ('Computer', 'Computer')], default=None, max_length=50)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('leave_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]