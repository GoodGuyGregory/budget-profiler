from django.shortcuts import render
from django.http import HttpResponse

from .models import Profile, Account, Debt, Expense, Goal


def index(request):
    return render(request, 'budgetprofiler/index.html')


def dashboard(request, username):
    username = Profile.objects.all()
    context = {
        'username': username[0],
    }
    return render(request, 'budgetprofiler/dashboard.html', context)


def summary(request, username):
    return HttpResponse("hello %s from summary view" % username)


def sheets(request, username):
    return HttpResponse("hello %s from sheets view" % username)


def expenses(request, username):
    return HttpResponse("hello %s from expenses view" % username)
