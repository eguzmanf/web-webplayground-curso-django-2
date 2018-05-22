from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/home.html"

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Mi super Web PlayGround"
        return context
    """

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "Mi super Web PlayGround Sobre Escrito"})


class SamplePageView(TemplateView):
    template_name = "core/sample.html"
