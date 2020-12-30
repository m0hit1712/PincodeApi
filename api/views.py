from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.


def find_in_file(state, district, taluk):
    filename = "./data/pincodes.json"
    with open(filename) as file:
        json_file = json.load(file)
        for item in json_file:
            if item['stateName'].lower() == state.lower():
                if item['districtName'].lower() == district.lower():
                    if item['taluk'].lower() == taluk.lower():
                        pincode = item['pincode']
                        return pincode
    return None


class GetPinCode(APIView):
    def get(self, request, state, district, taluk):
        state = state.replace("_", " ").lower()
        district = district.replace("_", " ").lower()
        taluk = taluk.replace("_", " ").lower()
        pincode = find_in_file(state, district, taluk)
        return Response({"pincode": pincode})

    def post(self, request, state, district, taluk):
        state = state.replace("_", " ").lower()
        district = district.replace("_", " ").lower()
        taluk = taluk.replace("_", " ").lower()
        pincode = find_in_file(state, district, taluk)
        return Response({"pincode": pincode})
