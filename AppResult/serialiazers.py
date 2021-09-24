# Modules
from rest_framework import serializers

# Model 
from AppResult.models import User

"""Create your Serializers here."""

# Register User Serializers
class RegisterUserSerializers(serializers.ModelSerializer):
    
    # Password Velidator
    password= serializers.CharField(max_length= 50, min_length= 6, write_only= True)

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
