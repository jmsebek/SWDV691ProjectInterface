from django.shortcuts import render
from userapplications.forms import ReportForm

# Create your views here.
def UserHomeView(request):
    return render(request, 'userhome.html')

def FlightEntryView(request):
    return render(request, 'flightentry.html')

def SummaryView(request):
    return render(request, 'summary.html')

def AccountDetailView(request):
    return render(request, 'accountdetail.html')

def MedicalView(request):
    return render(request, 'medical.html')

def ReportsView(request):
    form = ReportForm
    context={
        'form' : form
    }
    return render(request, 'reports.html', context)