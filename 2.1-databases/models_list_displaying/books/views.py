from django.shortcuts import render, redirect
from django.db.models import Count
from datetime import datetime
from .models import Book


def index(request):
    return redirect('books')


def books_view(request, date_filter=None):
    template = 'books/books_list.html'
    query = None

    if date_filter:
        try:
            query = datetime.strptime(date_filter, "%Y-%m-%d").date()
        except ValueError:
            return redirect('books')

    context = {
        'books': [],
        'prev_date': None,
        'next_date': None
    }

    if query:
        dates = list(Book.objects
                     .annotate(count=Count('pub_date'))
                     .values_list('pub_date', flat=True)
                     .distinct()
                     .order_by('pub_date'))
        try:
            i = dates.index(query)
            context['prev_date'] = datetime.strftime(dates[i - 1], "%Y-%m-%d") if i > 0 else None
            context['next_date'] = datetime.strftime(dates[i + 1], "%Y-%m-%d") if i + 1 != len(dates) else None
            context['books'] = Book.objects.all().filter(pub_date=query).order_by('pub_date')
        except:
            pass
    else:
        context['books'] = Book.objects.all().order_by('pub_date')

    return render(request, template, context)
