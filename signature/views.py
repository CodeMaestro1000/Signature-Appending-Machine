from functools import lru_cache
from django.db.models import fields
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import Request
from .forms import RequestForm
from django.urls import reverse
import random
import requests
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
    

class RequestPageView(CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'home.html'
    # fields = ['full_name', 'school_id', 'email', 'signatory', 'purpose']

class RequestSuccessView(TemplateView):
    template_name = 'request_sent.html'

class RequestsView(ListView):
    queryset = Request.objects.filter(status='pending').order_by('-date')
    template_name = 'requests.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class HistoryView(ListView):
    queryset = Request.objects.order_by('-time').filter(status='accepted') | Request.objects.filter(status='declined')
    template_name = 'history.html'

def random_gen():
  number = random.randrange(100000,900000,1)
  return number


def accept_request(request, pk):
    current_request = Request.objects.filter(pk=pk).first()
    signatory = current_request.signatory
    current_request.set_status('accepted')
    # convert number to string and append signature ID
    rand = str(random_gen())
    otp = rand + str(pk)
    receiver_email = current_request.email
    subject = "Signature Appending Request Accepted"
    message = """Hi there,
    Your request to use {}'s signature has been accepted.
    Please use {} as your OTP code to start appending.
    
    Kindly ignore this message if you didn't make a request.
    
    Regards,
    Signature Appending Team.""".format(signatory, otp)

    send_mail(subject, message, 
    from_email='futsignatureappender@gmail.com',
    recipient_list=[receiver_email]
    )
    
    requests.post('https://api.thingspeak.com/update.json', params={'api_key':'QROYHFSY12FUPYLP','field1':otp})
    return HttpResponseRedirect(reverse('history'))

def decline_request(request, pk):
    current_request = Request.objects.filter(pk=pk).first()
    current_request.decline_request()
    return HttpResponseRedirect(reverse('history'))





'''# Post data/OTP to thing speak
time.sleep(10)

# Get data/OTP to thing speak
response = requests.get('https://api.thingspeak.com/channels/1456194/fields/1.json?api_key=UNPMSZCZJF69MEUO&results=1')

print(response.text)

print(otp)'''




