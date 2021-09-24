# Import Module
from django.contrib import admin

# Model
from AppResult.models import User

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
        })
    )

    