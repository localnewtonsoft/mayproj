from django.shortcuts import render
from django.views.generic import TemplateView

class Index_view(TemplateView):
    template_name="webapp/index.html"