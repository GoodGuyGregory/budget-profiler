from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.dashboard, name='dashboard'),
    path('<str:username>/summary', views.summary, name='summary'),
    path('<str:username>/sheets', views.sheets, name='sheets'),
    path('<str:username>/expenses', views.expenses, name='expenses'),

]
