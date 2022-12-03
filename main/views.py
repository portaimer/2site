from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request, 'main/index.html')

def bani(request):
    return render(request, 'main/bani.html')

def houses(request):
    return render(request, 'main/houses.html')

def dom_iz_penobloka(request):
    return render(request, 'main/dom_iz_penobloka.html')

def otdelochnye_raboty(request):
    return render(request, 'main/otdelochnye_raboty.html')

def contact_us(request):
    global form
    context = {}
    if request.method == 'POST':
        pass
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'main/contact_us.html', context=context)