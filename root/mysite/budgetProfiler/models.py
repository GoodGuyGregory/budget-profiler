from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=50)
    earnings = models.FloatField(default=0)

    def __str__(self):
        return self.username

    def get_accounts(self):
        return self.account_set.all()


class Account(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=50)

    ACCOUNT_TYPES = (
        ('checking', 'Checking'),
        ('saving', 'Savings'),
        ('debit', 'Debit')
    )
    account_type = models.CharField(
        max_length=8,
        choices=ACCOUNT_TYPES,
        default=ACCOUNT_TYPES[2])
    account_balance = models.FloatField(default=0)

    def __str__(self):
        return self.account_name


class Debt(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    debt_name = models.CharField(max_length=50)
    balance_remaining = models.FloatField(default=0)
    interest = models.FloatField(default=0)

    def __str__(self):
        return self.debt_name


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

    def __str__(self):
        return self.expense_name


class Goal(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=50)
    goal_total = models.FloatField(default=0)
    balance_saved = models.FloatField(default=0)
    acomplish_date = models.DateField('completion date')
    payment_deductions = models.FloatField(default=0)

    def __str__(self):
        return self.goal_name
