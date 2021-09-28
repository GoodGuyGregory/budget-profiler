from django.contrib import admin

from .models import Profile, Account, Debt, Expense, Goal

admin.site.register(Profile)
admin.site.register(Account)
admin.site.register(Debt)
admin.site.register(Expense)
admin.site.register(Goal)
