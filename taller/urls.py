from django.urls import path
from .views import ListJobs, PreCitaView


urlpatterns = [
	path('operations/', ListJobs.as_view(), name="taller-list-jobs"),
	#http://127.0.0.1:8000/api/v1/operations/?niv__niv=00002904
	path('precita/', PreCitaView.as_view(), name="precita-list"),
	#http://127.0.0.1:8000/api/v1/precita/
]