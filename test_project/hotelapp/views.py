from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
# Create your views here.
from .serializers import *
from .models import *
from .utility import *

#FETCHING ALL OBJECTS FROM RESTAURANT MODEL AND ENCRYPTING THE RESPONSE
@api_view()
def Restaurantview(request):
    query=RestaurantModel.objects.all()
    a=[]
    for i in query:
        a.append({"id":i.id,"name":i.name,"valuation":i.valuation,"address":i.address})
    print(a)
    data=bytes(str(a),'utf-8')
    x=encryption(data)
    result=json.loads(x[0])
    key=x[1]
    y=decryption(x[0],key)
    return Response(result)

#DELETING THE RECORD WITH ID AND REUTURNING THE ENCRYPTED RESPONSE
@api_view()
def DeleteView(request,inp):
    try:
        query=RestaurantModel.objects.get(id=inp)
        query.delete()
        a=[{"status code":200,"Status_message":"Successfully deleted"}]
        data=bytes(str(a),'utf-8')
        x=encryption(data)
        result=json.loads(x[0])
        key=x[1]
        y=decryption(x[0],key)
        return Response(result)
    except:
        a=[{"status code":404,"Status_message":"No record with id = {}".format(inp)}]
        data=bytes(str(a),'utf-8')
        x=encryption(data)
        result=json.loads(x[0])
        key=x[1]
        y=decryption(x[0],key)
        return Response(result)

#FUNCTION FOR ADDING THE RECORDS
@api_view(['POST'])
def AddView(request):
    a=RestaurantSerializer(data=request.data)
    if a.is_valid():
        a.save()

        #Encryption and decryption for record in database
        record=bytes(str(a.data),'utf-8')
        r=encryption(record)
        encrypted_data=json.loads(r[0])
        encrypted_key=r[1]
        decrypt=decryption(r[0],encrypted_key)

        #Encryption for status response
        var=[{"status code":200,"Status_message":"The data stored in database successfully"}]
        data1=bytes(str(var),'utf-8')
        x=encryption(data1)
        result=json.loads(x[0])
        key=x[1]
    else:
        var=[{"status code":404,"Status_message":"The record failed to store in database"}]
        data1=bytes(str(var),'utf-8')
        x=encryption(data1)
        result=json.loads(x[0])
        key=x[1]
    return Response(result)

#VIEWING ALL THE OBJECTS IN RESTAURANT MODEL
@api_view()
def home(request):
    query=RestaurantModel.objects.all().order_by('name')
    a=[]
    for i in query:
        a.append({"id":i.id,"name":i.name,"valuation":i.valuation,"address":i.address})
    result=a
    return Response(result)