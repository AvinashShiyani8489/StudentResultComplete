''' * Import Modules * '''

# By Default 
from django.shortcuts import render

# Util for sending E-Mails
from .utils import Util

# Model - User
from AppResult.models import User, StudentRegistrationModel, StudentResultModel

# Serializer 
from AppResult.serialiazers import (
    RegisterUserSerializers,                                               # Custom User Register Serializer
    StudentRegistrationSerializers,                                        # Student Registrations Serializer
    StudentResultSerializers,                                              # Student Result Serializers 
    )

# Rest Framework 
from rest_framework import status                                           # Set HTTP Status
from rest_framework import generics                                         # Set Generic Method
from rest_framework.response import Response                                # Response HTTP status
from rest_framework import viewsets                                         # CRUD view route
from rest_framework.permissions import IsAuthenticated

# Simple Json Web Token
from rest_framework_simplejwt.tokens import RefreshToken                    # Send Token for Email verification
from rest_framework_simplejwt.authentication import JWTAuthentication       # Show data with Token 

# System Modules 
from django.contrib.sites.shortcuts import get_current_site                 # For our Domain for Email Verification
from django.conf import settings                                            # Use Setting for Screte key

# URLS
from django.urls import reverse                                             # Reverse App.Urls - Email Verification this use in Class EmailVerfications

# Json Web token
import jwt                                                                  # Decode Token for verification





''' * Register/SignUp Users & Send Email Verification Token * '''
class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterUserSerializers

    # POST Method for User Registertion
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user= User.objects.get(email=user_data['email'])                    # Fatch Email from Database 

        token = RefreshToken.for_user(user).access_token                    # Token(refresh and access) for User

        current_site= get_current_site(request).domain                      # Use Domain set in setting.py 
        relativeLink= reverse('email-verify')                               # Reverse Url from App.urls
        
        absurl= 'http://'+current_site+relativeLink+"?token="+str(token)    # Send link and token thourgh Email
        
        # Email Body with token and reverse link
        email_body= 'hi' + user.username + 'Use link below to verify your email \n' + absurl

        # Email Format
        data= {
            'email_body': email_body,
            'to_email': user.email,
            'email_subject':'verify your email'}

        Util.send_email(data)                                               # Send Email

        return Response(user_data,status=status.HTTP_201_CREATED)           # Give Status 


''' * Decode Token & Verify Email * '''
class VerifyEmail(generics.GenericAPIView):

    # Get Method For Links and Token
    def get(self, request):
        token = request.GET.get('token')                                                            # Get Token
        
        try:

            payload= jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')                      # Decode Token
            user= User.objects.get(id=payload['user_id'])                                           # Get id - Email 
            
            # verify Email conditions
            if not user.is_verified:
                user.is_verified= True
                user.save()

            return Response({'email':'successfully activated'}, status=status.HTTP_200_OK)          # Get Status if Success

        # Handle Error     
        except jwt.ExpiredSignatureError:                                                           # Expiry Token
            return Response({'error':'Activation Expreied'}, status=status.HTTP_400_BAD_REQUEST)

        except jwt.exceptions.DecodeError:                                                          # Error for decode token
            return Response({'error':'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)



# Student Regitration API 
class StudentRegistrationAPIView(viewsets.ModelViewSet):

    queryset= StudentRegistrationModel.objects.filter(is_active=True)
    serializer_class= StudentRegistrationSerializers
    authentication_classes= [JWTAuthentication]
    permission_classes= [IsAuthenticated]

    # Delete Data - is_active = False
    def destroy(self, request, *args, **kwargs):
        student = self.get_object()
        student.is_active = False
        student.save()
        return Response(data='delete success')

class StudentResultAPIView(viewsets.ModelViewSet):

    queryset= StudentResultModel.objects.filter(is_active=True)
    serializer_class= StudentResultSerializers
    authentication_classes= [JWTAuthentication]
    permission_classes= [IsAuthenticated]

    # Delete Data - is_active = False
    def destroy(self, request, *args, **kwargs):
        result = self.get_object()
        result.is_active = False
        result.save()
        return Response(data='delete success')
    
