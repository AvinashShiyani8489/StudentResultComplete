# By Default 
from django.db import models

# Authentication for Creating Custom User model 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Set RegexValidator in Fields
from django.core.validators import RegexValidator




"""Create your models here."""

# Create User Manager base on Old user Manager
class UserManager(BaseUserManager):

    # Create User 
    def create_user(self, username, email, role,first_name, last_name, birth_date, gender, mobile, address, area, city, pincode, password=None):

        # if conditions for checking value is not null.
        if username is None:
            raise TypeError("User should have a UserName")
        if email is None:
            raise TypeError("User should have a Email")
        if role is None:
            raise TypeError("User should have a Role")
        if first_name is None:
            raise TypeError("User should have a First Name")
        if last_name is None:
            raise TypeError("User should have a Last Name")
        if birth_date is None:
            raise TypeError("User should have a Birth Date")
        if gender is None:
            raise TypeError("User should have a Gender")
        if mobile is None:
            raise TypeError("User should have a Mobile")
        if address is None:
            raise TypeError("User should have a Address")
        if area is None:
            raise TypeError("User should have a Area")
        if city is None:
            raise TypeError("User should have a city")    
        if pincode is None:
            raise TypeError("User should have a Pincode")
        
        # For Saving 
        user= self.model(
            username = username,
            email= self.normalize_email(email),
            role= role,
            first_name = first_name,
            last_name = last_name,
            birth_date = birth_date,
            gender = gender,
            mobile = mobile,
            address = address,
            area = area,
            city = city,
            pincode = pincode
        )
        user.set_password(password)
        user.save()
        return user


    # Create SuperUser
    def create_superuser(self, username, email, role,first_name, last_name, birth_date, gender, mobile, address, area, city, pincode, password=None):
        
        # if conditions for checking value is not null.
        if password is None:
            raise TypeError("password should not be none")

        # For Saving Method
        user=self.create_user(username, email, role, first_name, last_name, birth_date, gender, mobile, address, area, city, pincode, password)
        user.is_active= True
        user.is_superuser= True
        user.is_staff= True
        user.save()
        return user

# Create User Model 
class User(AbstractBaseUser,PermissionsMixin):

    # Fields Name and Fields with validators

    # User Name
    username= models.CharField(
        max_length=50, 
        unique=True,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9@.+-_]*$',
                message='Username must be Alphanumeric',
                code='invalid_username'
            )
        ])

    # Email
    email= models.EmailField(
        max_length=254, 
        unique= True,
        validators=[
            RegexValidator(
                regex="^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$",
                message='Email must be properly(user@domanname.com or in or edu)',
                code='invalid_Email'
            )
        ])

    # Role
    Select_Role = [
        (None, "Choose Your Role"),
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("management", "Management Staff")]

    role= models.CharField(
        max_length=50,
        choices=Select_Role,
        default=None)

    # First Name
    first_name= models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='First Name must be Alphabet',
                code='invalid_firstName'
            )
        ])

    # Last Name
    last_name= models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='First Name must be Alphabet',
                code='invalid_firstName'
            )
        ])

    # Birth Date
    birth_date= models.DateField(auto_now=False, auto_now_add=False)

    # Gender 
    Select_Gender = [
        (None, "Choose your gender"),
        ("male", "Male"),
        ("female", "Female"),
        ("prefer not to say", "prefer not to say")]

    gender= models.CharField(
        max_length= 50,
        choices=Select_Gender,
        default= None)

    # Mobile 
    mobile= models.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex='^[0-9+]*$',
                message='Only Numberic or start with + ',
                code='Invalid_MobileNumber'
            )
        ])

    # Address
    address= models.TextField(max_length=300)
    
    # Area Name / Landmark
    area= models.CharField(max_length=50)

    # City
    city= models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='City Name must be Alphabet',
                code='Invalid City Name'
            )
        ])

    # Pincode
    pincode= models.CharField(
        max_length=6,
        validators=[
            RegexValidator(
                regex='^[0-9]*$',
                message='Only Numberic',
                code='Invalid Pincode'
            )
        ])
    

    # Authentication Fields 
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    Updated_at= models.DateTimeField(auto_now=True)

    # Set Username for LogIn and Required Fields
    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS= ['email', 'role', 'first_name', 'last_name', 'birth_date', 'gender', 'mobile', 'address', 'area', 'city', 'pincode']

    objects=UserManager()

    def __str__(self):
        return self.username
        
    def tokens(self):
        return ''

