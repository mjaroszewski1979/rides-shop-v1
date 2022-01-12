from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Car, Category
from .filters import CarFilter
from .utilities import send_email
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        contact_name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_email(email_from=email, name=contact_name, subject=message)
        messages.success(request, 'Thank you ' + contact_name + ' for your message. We will reply to you as soon as possible at ' + email + '.')
        return redirect('index')

    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def expedition(request):
    return render(request, 'expedition.html')

def racing(request):
    return render(request, 'racing.html')

def speed(request):
    return render(request, 'speed.html')

def vintage(request):
    return render(request, 'vintage.html')

def cars(request):
    context = {}
    filter = CarFilter(request.GET, queryset=Car.objects.all())
    context['filter'] = filter
    paginator = Paginator(filter.qs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'cars.html', context=context)

def car(request, car_slug):
    car = get_object_or_404(Car, slug=car_slug)
    return render(request, 'car.html', {'car': car})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    cars = category.cars.all()
    paginator = Paginator(cars, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'category.html', {'page_obj': page_obj})

def page_not_found(response, exception):
    return render(response, '404.html')

def server_error(response):
    return render(response, '500.html')


