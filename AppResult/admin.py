# Import Module
from django.contrib import admin

# Model
from AppResult.models import User, StudentRegistrationModel, TeacherModel, StudentResultModel

from django.contrib.auth.admin import UserAdmin

''' Register your models here.'''

# Register User Model
@admin.register(User)
class UserAdmin(UserAdmin):
    
    # See Fields and data in Index of Model 
    list_display= ['id', 'username', 'first_name', 'last_name', 'email']

    # Set Fields Arrangement 
    fieldsets = (
        # User Informations
        ('Register Info:', {
            'fields': ('username', 'email', 'password')
        }),

        # Personal Informations
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'birth_date', 'gender'),
        }),

        # Contact Informations
        ('Contact Info', {
            'fields': ('mobile', 'address', 'area', 'city', 'pincode'),
        }),

        # Other Informations
        ('Other Info', {
            'fields': ('role',),
        }),

        # Login Informations
        ('Login Info', {
            'fields': ('last_login',),
        }),

        # Permissions 
        ('Permissions', {
            'fields': ('user_permissions', 'groups'),
        }),

        # Authentications
        ('Authentication', {
            'fields': ('is_active', 'is_superuser', 'is_staff', 'is_verified',),
        }))



# Student Registration Admin
@admin.register(StudentRegistrationModel)
class StudentRegistrationAdmin(admin.ModelAdmin):

    # See Fields and data in Index of Model 
    list_display= ["student_id", "student_first_name", 'student_last_name', 'admission_std', 'admission_stream']

    # Set Fields Arrangement 
    fieldsets = (
        # User Informations
        ('Register Info:', {
            'fields': ('student_id',)
        }),

        # Student Personal Informations
        ('Student Personal Info', {
            'fields': ('student_first_name', 'student_middel_name', 'student_last_name', 'gender', 'birth_date'),
        }),

        # Parents Informations
        ('Parents Info', {
            'fields': ('relations', 'parents_first_name', 'parents_last_name', 'mobile', 'email'),
        }),

        # Contact Informations
        ('Contact Info', {
            'fields': ('address', 'area', 'city', 'pincode'),
        }),

        # Admission Deatils
        ('Admission Deatails', {
            'fields': ('admission_std', 'admission_stream'),
        }),

        # Previous Edcucation
        ('Previous Edcucation', {
            'fields': ('previous_std','percentage'),
        }),

        # School Deatils 
        ('Admission Durations', {
            'fields': ('admission_date','leave_date'),
        }),

        # Authentications
        ('Authentication', {
            'fields': ('is_active', ),
        }))


# Teacher Admin 
@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display= ['teacher_id', 'first_name', 'last_name', 'subject_name']

    
    # Set Fields Arrangement 
    fieldsets = (
        # User Informations
        ('Register Info:', {
            'fields': ('teacher_id',)
        }),

        # Student Personal Informations
        ('Teacher Info', {
            'fields': ('first_name', 'last_name', 'gender', 'birth_date'),
        }),

        # Contact Informations
        ('Contact Info', {
            'fields': ('mobile', 'email', 'address', 'area', 'city', 'pincode'),
        }),

        # School Deatils 
        ('Teacher Details', {
            'fields': ('subject_name', 'join_date', 'leave_date'),
        }),

        # Authentications
        ('Authentication', {
            'fields': ('is_active', ),
        })
    )


# Student Result
@admin.register(StudentResultModel)
class StudentResultAdmin(admin.ModelAdmin):
    list_display= ['id', 'student_first_name', 'student_last_name', 'admission_std', 'teacher_id', 'result']

    # Set Fields Arrangement 
    fieldsets = (

        # Student Details 
        ('Student Info', {
            'fields': ('student_id', 'student_first_name', 'student_last_name'),
        }),

        # Standard
        ('Class Info', {
            'fields': ('admission_std', 'admission_stream'),
        }),

        # Teacher Details 
        ('Teacher Details', {
            'fields': ('teacher_id', 'subject_name'),
        }),

        # Result Info 
        ('Result Informations', {
            'fields': ('english' ,'maths', 'science', 'computer', 'total_marks', 'result', 'percentage'),
        }),

    )
