from django.shortcuts import render
from django.core import serializers
import json
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .models import UserProfile
from .serializers import UserProfileInputSerializer, UserProfileOutputSerializer
import djangoapi.utils as utils
from rest_framework.parsers import JSONParser 
from django.utils.encoding import smart_str
from django.contrib.auth.hashers import make_password

def userprofile_get(id):
    userprofile = UserProfile.objects.get_user(id)
    serializer = UserProfileOutputSerializer(userprofile, many=True)
    return utils.good_response(serializer.data)

def userprofile_delete(id):
    try:
        userprofile = UserProfile.objects.get(pk=id)
    except UserProfile.DoesNotExist:
        return utils.empty_bad_response()
    
    res = userprofile_get(id)
    # serializer = UserProfileInputSerializer(UserProfile.objects.get_user(id), many=True)
    userprofile.delete()
    # return utils.good_response(serializer.data)
    return res

def userprofile_post(request):
    userprofile_data = JSONParser().parse(request)

    pwd = make_password(userprofile_data['password'])
    userprofile_data['password'] = pwd

    userprofile_serializer = UserProfileInputSerializer(data=userprofile_data)
    if userprofile_serializer.is_valid():
            userprofile_serializer.save() 
            id = userprofile_data['id']
            serializer = UserProfileOutputSerializer(UserProfile.objects.get_user(id), many=True)
            return utils.good_response(serializer.data, 201) 
    return utils.bad_response(userprofile_serializer.errors)   

def userprofile_put(request, id):
    try:
        userprofile = UserProfile.objects.get(pk=id)
    except UserProfile.DoesNotExist:
        return utils.empty_bad_response()

    # serialized_obj = eval(serializers.serialize('json', [userprofile]))
    # print(serialized_obj[0])
    userprofile_data = JSONParser().parse(request) 
    # userprofile_data.update(serialized_obj[0]['fields'])
    # print(userprofile_data, type(userprofile_data))
    # print(userprofile, type(userprofile))

    userprofile_serializer = UserProfileOutputSerializer(userprofile, data=userprofile_data, partial=True)
    if userprofile_serializer.is_valid():
            userprofile_serializer.save() 
            return utils.good_response(userprofile_serializer.data) 
    return utils.bad_response(userprofile_serializer.errors)         


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def get_userprofile(request):
    id = request.GET.get("id")
    if request.method == 'GET': return userprofile_get(id)
    elif request.method == 'PUT': return userprofile_put(request, id)
    elif request.method == 'POST': 
        if request.path == "/api/signup":
            return userprofile_post(request)
        else: 
            return utils.empty_bad_response()
    elif request.method == 'DELETE': return userprofile_delete(id)
