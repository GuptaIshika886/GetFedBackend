
from django.shortcuts import render
from . models import RegisteredUsers
from .serializers import RegisteredUsersSerializers
from . models import Canteen
from . models import RegisteredCntnOwners
from . serializers import CanteenSerializers
from . models import Categories
from . serializers import CategoriesSerializers
from . models import ViewProfile
from . serializers import ViewProfileSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json
from . serializers import RegisteredCntnOwnersSerializers
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

@csrf_exempt
def usersDetail(request):
    many=True
    if request.method=='GET':
        regusers=RegisteredUsers.objects.all()
        serializer=RegisteredUsersSerializers(regusers,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
        
    if request.method=='POST':
        jsonData=JSONParser().parse(request)
        serializer=RegisteredUsersSerializers(data=jsonData)
        # print(jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)

@csrf_exempt
def cntnOwnersDetail(request):
    many=True
    if request.method=='GET':
        regowners=RegisteredCntnOwners.objects.all()
        serializer=RegisteredCntnOwnersSerializers(regowners,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
        
    if request.method=='POST':
        jsonData=JSONParser().parse(request)
        serializer=RegisteredCntnOwnersSerializers(data=jsonData)
        # print(jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)
        
def post(request):
    # current_location = request.data.get('current_location')
    # destination = request.data.get('destination')
    current_location='ShantaPuri'
    destination='Shanus'  
        # Initialize the Google Maps client
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
        
        # Get the route between the two points
    directions_result = gmaps.directions(current_location, destination, mode="driving")
        
        # Parse the route information and return it as JSON
    route = []
    for leg in directions_result[0]['legs']:
        for step in leg['steps']:
            route.append(step['html_instructions'])
    return Response({'route': route})

def canteenDetail(request):
    many=True
    if request.method=='GET':
        can=Canteen.objects.all()
        serializer=CanteenSerializers(can,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method=='POST':
        jsonData=JSONParser().parse(request)
        serializer=CanteenSerializers(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JSONRenderer(serializer.data)
        else:
            return JSONRenderer(serializer.errors)

def categoriesDetail(request):
    many=True
    if request.method=='GET':
        catDetail=Categories.objects.all()
        serializer=CategoriesSerializers(catDetail,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method=='POST':
        jsonData=CategoriesSerializers(request)
        serializer=CategoriesSerializers(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JSONRenderer(serializer.data)
        else:
            return JSONRenderer(serializer.errors)

@csrf_exempt       
def viewProfileDetail(request):
    many=True
    if request.method=='GET':
        vpDetail=ViewProfile.objects.all()
        serializer=ViewProfileSerializers(vpDetail,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
        
    if request.method=='POST':
        jsonData=JSONParser().parse(request)
        serializer=ViewProfileSerializers(data=jsonData)
        # print(jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)

