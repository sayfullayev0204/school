from django.shortcuts import render
from django.views.generic import TemplateView

class SelectClass(TemplateView):
    template_name = 'sinf.html'
    context_object_name = []

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['data'] = [i+1 for i in range(11)]
            return context

def home(request):
    return render(request , 'home.html')
def sinf(request):
    return render(request , 'sinf.html')
def fan(request):
    return render(request , 'fan.html')
def uzifa(request):
    return render(request , 'vazifa.html')
def tek(request):
    return render(request , 'tek.html')
def info(request):
    return render(request , 'info.html')
