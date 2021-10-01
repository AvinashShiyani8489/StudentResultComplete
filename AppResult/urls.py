# By Default Modules
from django.urls import path,include

# Token For Login
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Router - API 
from rest_framework.routers import DefaultRouter

# App View 
from AppResult.views import (
   RegisterView,
   StudentResultAPIView,                                                                          # Register User View 
   VerifyEmail,                                                                           # Verify Email View 
   StudentRegistrationAPIView,                                                            # Student Registraion table 
   LoginAPIView,                                                                          # Login Views 
   )




""" * Set All URLS  * """


# Set Router for Views
router = DefaultRouter()

# Student Registration Router API
router.register("stureg", StudentRegistrationAPIView, basename="studentregistration")
router.register("result",StudentResultAPIView, basename="result")



urlpatterns = [

   # Register /SignUp User
   path('register/', RegisterView.as_view(), name='register'),                            

   # Verify Email- this link use in Sending Email.
   path('email-verify/',VerifyEmail.as_view(), name= 'email-verify'),   

   # Login User
   path('login/',LoginAPIView.as_view(), name= 'login'),                  
   
   # Set Router URL
   path("api/",include(router.urls)),
   path("auth/", include("rest_framework.urls", namespace="rest_framework")),

   # Generate Access Token  
   path("loginjwt/", TokenObtainPairView.as_view(), name="loginjwt"),
   # Generate Refresh Token
   path("refresh/",TokenRefreshView.as_view(), name="refreshtoken"),
]