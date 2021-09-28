# Generated by Django 3.2.6 on 2021-09-27 07:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppResult', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRegistrationModel',
            fields=[
                ('student_id', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('student_first_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_firstName', message='First Name must be Alphabet', regex='^[a-zA-Z]*$')])),
                ('student_middel_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_firstName', message='First Name must be Alphabet', regex='^[a-zA-Z]*$')])),
                ('student_last_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_firstName', message='First Name must be Alphabet', regex='^[a-zA-Z]*$')])),
                ('gender', models.CharField(choices=[(None, 'Choose your gender'), ('male', 'Male'), ('female', 'Female'), ('prefer not to say', 'prefer not to say')], default=None, max_length=50)),
                ('birth_date', models.DateField()),
                ('relations', models.CharField(choices=[(None, 'Choose your Relations'), ('father', 'Father'), ('mother', 'Mother'), ('brother', 'Brother'), ('Sister', 'Sister')], default=None, max_length=50)),
                ('parents_first_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_firstName', message='First Name must be Alphabet', regex='^[a-zA-Z]*$')])),
                ('parents_last_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_firstName', message='First Name must be Alphabet', regex='^[a-zA-Z]*$')])),
                ('mobile', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(code='Invalid_MobileNumber', message='Only Numberic or start with + ', regex='^[0-9+]*$')])),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_Email', message='Email must be properly(user@domanname.com or in or edu)', regex='^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$')])),
                ('address', models.TextField()),
                ('area', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='Invalid City Name', message='City Name must be Alphabet', regex='^[a-zA-Z]*$')])),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(code='Invalid Pincode', message='Only Numberic', regex='^[0-9]*$')])),
                ('admission_std', models.CharField(choices=[(None, 'Choose Student STD.'), ('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5', '5th'), ('6', '6th'), ('7', '7th'), ('8', '8th'), ('9', '9th'), ('10', '10th')], default=None, max_length=50)),
                ('admission_stream', models.CharField(choices=[(None, 'Choose Student Stream'), ('Science', 'Science'), ('Math', 'Maths'), ('English', 'English'), ('Computer', 'Computer')], default=None, max_length=50)),
                ('previous_std', models.CharField(choices=[(None, 'Choose Student STD.'), ('u kg', 'Upper KinderGarten'), ('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5', '5th'), ('6', '6th'), ('7', '7th'), ('8', '8th'), ('9', '9th')], default=None, max_length=50)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('admission_date', models.DateField()),
                ('leave_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='Invalid City Name', message='City Name must be Alphabet', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_Email', message='Email must be properly(user@domanname.com or in or edu)', regex='^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_firstName', message='First Name must be Alphabet', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[(None, 'Choose your gender'), ('male', 'Male'), ('female', 'Female'), ('prefer not to say', 'prefer not to say')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_firstName', message='First Name must be Alphabet', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(code='Invalid_MobileNumber', message='Only Numberic or start with + ', regex='^[0-9+]*$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(code='Invalid Pincode', message='Only Numberic', regex='^[0-9]*$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[(None, 'Choose Your Role'), ('student', 'Student'), ('teacher', 'Teacher'), ('management', 'Management Staff')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be Alphanumeric', regex='^[a-zA-Z0-9@.+-_]*$')]),
        ),
    ]
