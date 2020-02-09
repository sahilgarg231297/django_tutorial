from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord

# Create your views here.


def index(request):
    my_dict = {"insert_me": "I am from views.py !"}
    return render(request, "first_app/index.html", context=my_dict)


def dashboard(request):
    access_records = AccessRecord.objects.order_by("date")
    records_dict = {"access_records": access_records}
    return render(request, "first_app/dashboard.html", context=records_dict)
