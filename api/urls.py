from django.urls import path, include
from . import views

urlpatterns = [
        path('getpincode/<str:state>/<str:district>/<str:taluk>', views.GetPinCode.as_view(), name="pincode_url"),
]


