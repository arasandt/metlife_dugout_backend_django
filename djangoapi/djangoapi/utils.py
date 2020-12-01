from rest_framework.response import Response
from rest_framework import status

def good_response(data):
    return Response({"data": data})
    # return Response({"data": data}, status=status.HTTP_400_BAD_REQUEST)
     
def empty_bad_response():
    return bad_response({})

def bad_response(data):
    return Response(data, status=status.HTTP_400_BAD_REQUEST)