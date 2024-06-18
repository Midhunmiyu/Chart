import html
import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import *

class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        fruits = Fruits.objects.all()
        fruits_labels = [fruit.name for fruit in fruits]
        fruits_prices = [fruit.price for fruit in fruits]
        context = {
            'fruits_labels': json.dumps(fruits_labels),
            'fruits_prices': json.dumps(fruits_prices)
        }
        # print(context, '*****')
        return render(request, self.template_name, context)