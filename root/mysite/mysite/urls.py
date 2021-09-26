from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('budgetProfiler/', include('budgetProfiler.urls')),
    path('admin/', admin.site.urls),
]
