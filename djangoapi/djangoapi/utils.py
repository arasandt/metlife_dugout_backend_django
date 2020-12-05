from rest_framework.response import Response
from rest_framework import status

def good_response(data, resp=status.HTTP_200_OK):
    return Response({"data": data}, status=resp)
     
def empty_bad_response():
    return bad_response({})

def bad_response(data):
    return Response(data, status=status.HTTP_400_BAD_REQUEST)