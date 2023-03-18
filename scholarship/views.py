from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Scholarship, ScholarshipFilter

title = settings.PROJECT_TITLE


def index(request):
    f = ScholarshipFilter(request.GET, queryset=Scholarship.objects.all())
    ctx = {
        'title': f'{title} | Home',
        'filter': f
    }
    return render(request, 'scholarship/index.html', ctx)


def scholarship(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('login')
    item = Scholarship.objects.get(id=id)
    ctx = {
        'title': f'{item.name.lower()}',
        'item': item
    }
    return render(request, 'scholarship/detail.html', ctx)
