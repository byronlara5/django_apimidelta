from django.urls import path
from .views import NivsById


urlpatterns = [
	path('niv/', NivsById.as_view(), name="niv-customer"),
	#http://127.0.0.1:8000/api/v1/niv/?search=101502282
	
]