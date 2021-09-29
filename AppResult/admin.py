# Import Module
from django.contrib import admin

# Model
from AppResult.models import User, StudentRegistrationModel, StudentResultModel

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

    readonly_fields= ['student_id', 'full_name']
    # Set Fields Arrangement 
    fieldsets = (
        # User Informations
        ('Register Info:', {
            'fields': ('student_id',),
        }),

        # Student Personal Informations
        ('Student Personal Info', {
            'fields': ('student_first_name', 'student_middel_name', 'student_last_name', 'gender', 'full_name', 'birth_date'),
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
            'fields': ('admission_date',),
        }),

        # Authentications
        ('Authentication', {
            'fields': ('is_active', ),
        }))


# Student Result
@admin.register(StudentResultModel)
class StudentResultAdmin(admin.ModelAdmin):
    list_display= ['id', 'student_name', 'result']
    readonly_fields= ['id', 'total_marks', 'result', 'percentage']

    # Set Fields Arrangement 
    fieldsets = (
        # User Informations
        ('Register Info:', {
            'fields': ('id',),
        }),

        # Student 
        ('Student Personal Info', {
            'fields': ('student_name',),
        }),

        # Subject Marks
        ('Subject Marks', {
            'fields': ('maths', 'english', 'science', 'computer',),
        }),

        # Result Informations
        ('Result Info', {
            'fields': ('total_marks', 'result', 'percentage',),
        }),

        # Authentications
        ('Authentication', {
            'fields': ('is_active', ),
        })
    )