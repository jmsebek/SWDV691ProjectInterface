from django.urls import path
from .views import UserHomeView, FlightEntryView, SummaryView, AccountDetailView, ReportsView, MedicalView

urlpatterns = [
    path("", UserHomeView, name="userhome"),
    path("flightentry/", FlightEntryView, name="flightentry"),
    path("summary/", SummaryView, name="summary"),
    path("accountdetail/", AccountDetailView, name="accountdetail"),
    path("medical/", MedicalView, name="medical"),
    path("reports/", ReportsView, name="reports"),
]