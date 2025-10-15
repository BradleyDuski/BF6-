from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Operator
# Create your views here.

class OperatorList(ListView):
    model = Operator
    template_name = "game/list.html"




class OperatorDetail(DetailView):
    model = Operator
    template_name = "game/details.html"