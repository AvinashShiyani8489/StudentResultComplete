# Modules
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

# Model 
from AppResult.models import StudentResultModel, User, StudentRegistrationModel

"""Create your Serializers here."""

# Register User Serializers
class RegisterUserSerializers(serializers.ModelSerializer):
    
    # Password Velidator
    password= serializers.CharField(max_length= 50, min_length= 6, write_only= True, style={'input_type': 'password', 'placeholder': 'Password'})
    
    class Meta:
        model= User
        fields= ['username', 'email', 'role', 'first_name', 'last_name', 'birth_date', 'gender', 'mobile', 'address', 'area', 'city', 'pincode', 'password']

    # Validate Data
    def validate(self, attrs):
        username= attrs.get('username','')
        email= attrs.get('email','')
        role= attrs.get('role', '')
        first_name= attrs.get('first_name','')
        last_name= attrs.get('last_name','')
        birth_date= attrs.get('birth_date', '')
        gender= attrs.get('gender','')
        mobile= attrs.get('mobile','')
        address= attrs.get('address', '')
        area= attrs.get('area','')
        city= attrs.get('city','')
        pincode= attrs.get('pincode', '')

        # Username Validation Error
        if not username.isalnum():
            raise serializers.ValidationError("The username should only contain alphanumeric characters")
        return attrs

    # Create user
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# Student Result 
class StudentResultSerializers(serializers.ModelSerializer):   

    # Set Validator & Styles in Fields 
    english = serializers.IntegerField(
        validators= [
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        style= {
            'input_type': 'number',
            'placeholder': "Enter Marks"
        })

    maths = serializers.IntegerField(
        validators= [
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        style= {
            'input_type': 'number',
            'placeholder': "Enter Marks"
        })

    computer = serializers.IntegerField(
        validators= [
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        style= {
            'input_type': 'number',
            'placeholder': "Enter Marks"
        })
    
    science = serializers.IntegerField(
        validators= [
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        style= {
            'input_type': 'number',
            'placeholder': "Enter  Marks"
        })

    class Meta:

        # Import Model
        model= StudentResultModel

        # Import Fields 
        fields= [
            'student_name',
            'english',
            'maths',
            'science',
            'computer',
            'total_marks',
            'result',
            'percentage'        
        ]

    # Read Only Field 
    total_marks = serializers.ReadOnlyField()
    result= serializers.ReadOnlyField()
    percentage= serializers.ReadOnlyField()

    

# Student Registration Serializers 
class StudentRegistrationSerializers(serializers.ModelSerializer):

    # Nested Serializers 
    Result = StudentResultSerializers(many=True, read_only=True)

    class Meta:
        # Import Model 
        model= StudentRegistrationModel
        # Import Fields 
        fields= [
            'student_id', 
            'student_first_name', 
            'student_middel_name', 
            'student_last_name', 
            'gender',
            'full_name',
            'birth_date', 
            'relations',
            'parents_first_name',
            'parents_last_name',
            'mobile',
            'email',
            'address',
            'area',
            'city',
            'pincode',
            'admission_std',
            'admission_stream',
            'previous_std',
            'percentage',
            'admission_date',
            'Result',
        ]

    # Read Only Field 
    full_name = serializers.ReadOnlyField()