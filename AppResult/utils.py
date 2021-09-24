# Modules for Emails
from django.core.mail import EmailMessage

''' * Delcartion of Email Setting for Verification * '''

class Util:
    @staticmethod

    # Send Email for verification Account 
    def send_email(data):
        
        # Email Format
        email = EmailMessage(
            subject= data['email_subject'],             # Email - Subject - from View > RegisterViews
            body= data['email_body'],                   # Email - Body from View > RegisterViews
            to=[data['to_email']]                       # Email - To 
        )
        email.send()                                    # Finally Send Email
