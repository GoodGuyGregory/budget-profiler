from django.shortcuts import render
from django.http import HttpResponse

from .models import Profile, Account, Debt, Expense, Goal


def index(request):
    return render(request, 'budgetprofiler/index.html')


def dashboard(request, username):
    # case insensitive with __iexact
    foundUsername = Profile.objects.get(username__iexact=username)
    foundUserid = foundUsername.id
    user_accounts = Account.objects.filter(profile=foundUserid)
    context = {
        'foundUsername': foundUsername,
        'user_accounts': user_accounts
    }
    return render(request, 'budgetprofiler/dashboard.html', context)


def summary(request, username):
    return HttpResponse("hello %s from summary view" % username)


def sheets(request, username):
    return HttpResponse("hello %s from sheets view" % username)


def expenses(request, username):
    return HttpResponse("hello %s from expenses view" % username)
