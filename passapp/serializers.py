from typing_extensions import Required
from venv import create
from rest_framework import serializers
from .models import CustomUser
from django.template.loader import render_to_string
import os
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail   # Used at send_mail method in use.
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created



# Serializer Class for Model.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True,
                        'required': False}  #write only--not show to anyone password/hashpassword
        }
         
# Override Method for managing .save() method with extra params.  
     
    def create(self, validated_data,*args,**kwargs):
        user = super(UserSerializer, self).create(validated_data)
        file_path = os.path.abspath('static/gitlab.png')  # static file path for file attach to the email.
        randomPassword= CustomUser.objects.make_random_password(length=7)
        accountData = {
            "email":validated_data['email'],
            "password":randomPassword
        }
        print(accountData)
        user.set_password(randomPassword)
        user.save()
        
# Code For Email Send.
        
        subject='Account Confirmation'
        html_message = render_to_string('accountConfirmation.html', {'account': accountData})     

        kwargs = dict(
          to=[user.email],
          from_email=None,
          subject=subject,
          body=html_message,
          alternatives=((html_message, 'text/html'),)
        )
        message = EmailMultiAlternatives(**kwargs)
        message.attach_file(file_path)
        message.send()               
        return user
    
# Code for Send Email With Custom HTML Template Only. 

        # send_mail(
        #         'Account Confirmation',
        #          'random text here',
        #         None,
        #         [user.email],
        #         fail_silently=False,
        #         html_message = render_to_string('accountConfirmation.html', {'account': accountData}),
              
        # )
                   
    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs, ):
            
        email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

        send_mail(
            # title:
            "Password Reset{title}".format(title="Link"),
            # message:
            email_plaintext_message,
            # from:
            None,
            # to:
            [reset_password_token.user.email]
    )


from django.contrib.auth.password_validation import validate_password
class ChangePasswordSerializer(serializers.Serializer):
    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password=serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
 

