from django.views.generic import TemplateView
from django.shortcuts import redirect

class HomePage(TemplateView):

    template_name = "home.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["welcome_message"] = "Welcome to campus accomodation review."
        return context

class AboutUs(TemplateView):
    template_name="about_us.html"
