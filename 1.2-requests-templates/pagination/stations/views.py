from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)
    context = {
        'bus_stations': [],
        'page': None,
        'page_size': page_size
    }

    with open(settings.BUS_STATION_CSV, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        paginator = Paginator(list(reader), page_size)
        page = paginator.get_page(page_number)
        context['bus_stations'] = page.object_list
        context['page'] = page

    return render(request, 'stations/index.html', context)
