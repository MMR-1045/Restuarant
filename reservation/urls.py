from django.urls import path
from . import views

app_name='reservation'

urlpatterns = [
    path('', views.reserv_table, name="reserv_table"),
]