from functools import lru_cache
from django.db.models import fields
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import Request
from .forms import RequestForm
from django.urls import reverse
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
    

class RequestPageView(CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'make_request.html'
    # fields = ['full_name', 'school_id', 'email', 'signatory', 'purpose']

class RequestSuccessView(TemplateView):
    template_name = 'request_sent.html'

class RequestsView(ListView):
    queryset = Request.objects.filter(status='pending').order_by('-time')
    template_name = 'requests.html'

class HistoryView(ListView):
    queryset = Request.objects.order_by('-time').filter(status='accepted') | Request.objects.filter(status='declined')
    template_name = 'history.html'


def accept_request(request, pk):
    current_request = Request.objects.filter(pk=pk).first()
    current_request.set_status('accepted')
    return HttpResponseRedirect(reverse('history'))

def decline_request(request, pk):
    current_request = Request.objects.filter(pk=pk).first()
    current_request.decline_request()
    return HttpResponseRedirect(reverse('history'))
