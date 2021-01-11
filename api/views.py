from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
import json

# Create your views here.


def find_in_json_file(state, district, taluk):
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

def find_in_csv_file(state, district, taluk):
    filename = "./data/pincodes_small.csv"
    with open(filename, newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            if state == row["statename"] or state == row["circlename"]:
                if district == row["DistrictName"] or district == row["regionname"]:
                    if taluk == row["divisionname"] or taluk == row["Taluk"]:
                        pincode = row["pincode"]
                        return pincode
    return None

class GetPinCode(APIView):
    def get(self, request, state, district, taluk):
        state = state.replace("_", " ").lower()
        district = district.replace("_", " ").lower()
        taluk = taluk.replace("_", " ").lower()
        pincode = find_in_json_file(state, district, taluk)
        if not pincode:
            find_in_csv_file(state, district, taluk)
        return Response({"pincode": pincode})

    def post(self, request, state, district, taluk):
        state = state.replace("_", " ").lower()
        district = district.replace("_", " ").lower()
        taluk = taluk.replace("_", " ").lower()
        pincode = find_in_json_file(state, district, taluk)
        if not pincode:
            find_in_csv_file(state, district, taluk)

        return Response({"pincode": pincode})

class GetDistricts(APIView):
    def get(self, request, state):
        state = state.replace("_", " ").lower()

    def post(self, request, state):
        state = state.replace("_", " ").lower()

class GetStates(APIView):
    def get(self, request, country):
        country = country.replace("_", " ").lower()

    def post(self, request, country):
        country = country.replace("_", " ").lower()

class GetTaluk(APIView):
    def get(self, request, district):
        district = district.replace("_", " ").lower()

    def post(self, request, district):
        district = district.replace("_", " ").lower()








