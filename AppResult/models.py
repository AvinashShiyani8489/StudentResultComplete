# By Default 
from django.db import models

# Authentication for Creating Custom User model 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Set RegexValidator in Fields
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from rest_framework.fields import ReadOnlyField




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


# Student Registrations Model
class StudentRegistrationModel(models.Model):

    # Fields with Validators 
    
    student_id= models.AutoField(primary_key=True)
    
    # Personal 
    student_first_name= models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='First Name must be Alphabet',
                code='invalid_firstName'
            )
        ])

    student_middel_name= models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='First Name must be Alphabet',
                code='invalid_firstName'
            )
        ])

    student_last_name= models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='First Name must be Alphabet',
                code='invalid_firstName'
            )
        ])

    Select_Student_Gender = [
        (None, "Choose your gender"),
        ("male", "Male"),
        ("female", "Female"),
        ("prefer not to say", "prefer not to say")]
    gender= models.CharField(
        max_length= 50,
        choices=Select_Student_Gender,
        default= None)
    
    full_name = models.CharField(max_length=500, null=True, blank=True)

    birth_date= models.DateField(auto_now=False, auto_now_add=False)

    # Parents Details
    Select_Relations = [
        (None, "Choose your Relations"),
        ("father", "Father"),
        ("mother", "Mother"),
        ("brother", "Brother"),
        ("Sister", "Sister")]        
    relations= models.CharField(
        max_length=50,
        choices=Select_Relations,
        default=None)

    parents_first_name= models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='First Name must be Alphabet',
                code='invalid_firstName'
            )
        ])

    parents_last_name= models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='First Name must be Alphabet',
                code='invalid_firstName'
            )
        ])
    
    mobile= models.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex='^[0-9+]*$',
                message='Only Numberic or start with + ',
                code='Invalid_MobileNumber'
            )
        ])
    
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

    # Contact Information
    address= models.TextField()

    area= models.CharField(max_length=50)
    
    city= models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='City Name must be Alphabet',
                code='Invalid City Name'
            )
        ])
    
    pincode= models.CharField(
        max_length=6,
        validators=[
            RegexValidator(
                regex='^[0-9]*$',
                message='Only Numberic',
                code='Invalid Pincode'
            )
        ])

    #Education Details 
    
        # Admission Now
    Select_Std = [
        (None, "Choose Student STD."),
        ("1", "1st"),
        ("2", "2nd"),
        ("3", "3rd"),
        ("4", "4th"),
        ("5", "5th"),
        ("6", "6th"),
        ("7", "7th"),
        ("8", "8th"),
        ("9", "9th"),
        ("10", "10th")]   
    admission_std= models.CharField(
        max_length=50,
        choices=Select_Std,
        default=None)

    Select_Stream= [
        (None, "Choose Student Stream"),
        ("Science", "Science"),
        ("Math", "Maths"),
        ("English", "English"),
        ("Computer", "Computer")]

    admission_stream= models.CharField(
        max_length=50,
        choices=Select_Stream,
        default=None)

    

        # Previous Details
    Select_Previous_Std = [
        (None, "Choose Student STD."),
        ("u kg", "Upper KinderGarten"),
        ("1", "1st"),
        ("2", "2nd"),
        ("3", "3rd"),
        ("4", "4th"),
        ("5", "5th"),
        ("6", "6th"),
        ("7", "7th"),
        ("8", "8th"),
        ("9", "9th")]
         
    previous_std= models.CharField(
        max_length=50,
        choices=Select_Previous_Std,
        default=None)

    percentage= models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ])


    #School Deatils
    admission_date= models.DateField(auto_now_add=False,auto_now= False)
    
    
    #Other Details 
    is_active= models.BooleanField(default=True)


    # Capitalize 
    def save(self, *args, **kwargs):
        for field_name in ['student_first_name', 'student_middel_name', 'student_last_name', 'parents_first_name', 'parents_last_name', 'address', 'area', 'city',]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.title())


        self.full_name = self.student_first_name + " " + self.student_middel_name + " " + self.student_last_name

        super(StudentRegistrationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name

# Student Result 
class StudentResultModel(models.Model):

   
    # Student Details 
    student_name= models.ForeignKey(StudentRegistrationModel, on_delete=models.CASCADE, related_name= "Result", unique=True)
    
    # Mark of Subject with Validator
    english= models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ])
    
    maths= models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ])
    
    science= models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ])
    
    computer= models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ])
    

    total_marks= models.IntegerField(null=True, blank=True)

    result= models.CharField(max_length=50,null=True, blank=True)

    percentage= models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
  
    # Calculate Marks & Capitalize 
    def save(self, *args, **kwargs):

        # Calculate 4 subject marks and store in total marks 
        self.total_marks = self.maths + self.science + self.english + self.computer

        # Result-  Pass Or Fail 
        if self.maths < 40 or self.science < 40 or self.english < 40 or self.computer < 40:
            self.result = "Fail"
        else:
            self.result = "Pass"
        
        # Percentage 
        if self.result == "Pass":
            self.percentage = self.total_marks/4
        else:
            self.percentage = 0    

            
        # Save Method      
        super(StudentResultModel, self).save(*args, **kwargs)

    
