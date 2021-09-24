# By Default Modules
from django.urls import path,include

# App View 
from AppResult.views import (
   RegisterView,                                                                          # Register User View 
   VerifyEmail)                                                                           # Verify Email View 

""" * Set All URLS  * """

urlpatterns = [

   # Register /SignUp User
   path('register/', RegisterView.as_view(), name='register'),                            

   # # Verify Email- this link use in Sending Email.
   path('email-verify/',VerifyEmail.as_view(), name= 'email-verify'),                     
   
]