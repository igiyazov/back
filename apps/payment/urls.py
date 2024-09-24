from django.urls import path

from apps.payment.views import get_link, check_link, check_status

urlpatterns = [
    path('generate_link', get_link),
    path('check_link', check_link),
    path('check_status', check_status),
]
