from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET'])
def health(request: Request) -> Response:
    if request.method != 'GET':
        return Response({"status": "failed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return Response({"states": "OK"}, status=status.HTTP_200_OK)



