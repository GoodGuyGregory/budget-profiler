from django.db import models


class Profile(models.Model):
    username = models.CharField(max_Length=50)
    earnings = models.FloatField(default=0)


class Account(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=50)
    CHECKING = 'checking'
    SAVING = 'saving'
    DEBIT = 'debit'
    ACCOUNT_TYPES = [
        (CHECKING, 'Checking')
        (SAVING, 'Savings')
        (DEBIT, 'Debit')
    ]
    account_type = models.CharField(
        max_length=8,
        choices=ACCOUNT_TYPES,
        default=DEBIT)
    account_balance = models.FloatField(default=0)


class Debt(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    debt_name = models.CharField(max_length=50)
    balance_remaining = models.FloatField(default=0)
    interest = models.FloatField(default=0)


class Expense(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=50)
    cost = models.FloatField(default=0)
    OCCURANCE_RATES = (
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('bi-weekly', 'Bi-weekly')
    )
    occurance_rate = models.CharField(
        max_length=9,
        choices=OCCURANCE_RATES,
        default=OCCURANCE_RATES[1])


class Goal(models.Model):
    profile = models.ForeignKey(Profile, on_delete=CASCADE)
    goal_name = models.CharField(max_length=50)
    goal_total = models.FloatField(default=0)
    balance_saved = models.FloatField(default=0)
    acomplish_date = models.DateTimeField('completion date')
    payment_deductions = models.FloatField(default=0)
