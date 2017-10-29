from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from mailing.models import EmailSubscriber
from django.core.exceptions import ValidationError
# Create your views here.


class EmailView(View):
    
    def post(self, request):
        
        email_subscriber = EmailSubscriber(email = request.POST.get('email', None))
        
        try:
            email_subscriber.full_clean()
            email_subscriber.save()
            
            response = {"message":"Thank you for signing up"}
            
        except ValidationError as e:
            
            response = e.message_dict
        
        
        return JsonResponse(response)
    