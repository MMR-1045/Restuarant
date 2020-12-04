from django.shortcuts import render
from.models import Reservation
from.forms import ReservationTableForm
# Create your views here.
# from reservation.models import Reservation

def reserv_table(request):
    reseve_form=ReservationTableForm()

    if request.method=='POST':
        reseve_form=ReservationTableForm(request.POST)

    if reseve_form.is_valid():
        reseve_form.save()
    context={'form':reseve_form}
    return render(request,'reservation/reservation.html',context)