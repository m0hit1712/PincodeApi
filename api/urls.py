from django.urls import path, include
from . import views

urlpatterns = [
        path('getpincode/<str:state>/<str:district>/<str:taluk>', views.GetPinCode.as_view(), name="pincode_url"),
        path('getstates/<str:country>', views.GetDistricts.as_view(), name="state_url"),
        path('getdistricts/<str:state>', views.GetStates.as_view(), name="district_url"),
        path('gettaluks/<str:district>', views.GetTaluk.as_view(), name="taluk_url"),
]


