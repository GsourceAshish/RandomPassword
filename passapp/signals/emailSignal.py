# from django.core.mail import EmailMessage
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.http import request
# from django.template import Context, context
# from django.template.loader import get_template,render_to_string

# from passapp.models import CustomUser
# import json
# from django.core.mail import EmailMessage
# from django.template import loader





# def sendAccountConfirmation(sender, instance, **kwargs):
#     data = json.dumps(instance)

#     # template = loader.get_template('accountConfirmation.html')
#     # context=Context({'account':data})
#     # content=template.render(context)
     
#     # ctx={
#     #     'account':data
#     # } 
#     message = get_template('templates/accountConfirmation.html').render(context({'account':data}))
#     print(message)
#     mail = EmailMessage(
#         subject="Order confirmation",
#         body=message,
#         from_email=None,
#         to=[data.email],
#         #reply_to=[EMAIL_ADMIN],
#     )
#     mail.content_subtype = "text/html"
#     return mail.send()  
    
   