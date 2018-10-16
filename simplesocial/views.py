from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class TestView(TemplateView):
    template_name = "test.html"

class ThanksView(TemplateView):
    template_name = "thanks.html"
