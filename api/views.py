from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.

class GetPinCode(APIView):
        def get(self, request, state, district, taluk):
                self.state = state.replace("_"," ").lower()
                self.district = district.replace("_"," ").lower()
                self.taluk = taluk.replace("_"," ").lower()
                pincode = self.return_pincode()
                return Response({"pincode": pincode})

        def post(self, request, state, district, taluk):
                self.state = state.replace("_"," ").lower()
                self.district = district.replace("_"," ").lower()
                self.taluk = taluk.replace("_"," ").lower()
                pincode = self.return_pincode()
                return Response({"pincode": pincode})
                
        def return_pincode(self):
                filename = "./data/pincodes.json"
                with open(filename) as file:
                        json_file = json.load(file)
                        for item in json_file:
                                if item['stateName'].lower() == self.state.lower():
                                        if item['districtName'].lower() == self.district.lower():
                                                if item['taluk'].lower() == self.taluk.lower():
                                                        pincode = item['pincode']
                                                        return pincode
                return None






