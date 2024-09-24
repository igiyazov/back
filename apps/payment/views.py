import random
import string

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.payment.utils import generate_link

val = 0


@api_view(['GET'])
def get_link(request):
    # code to get link
    link = generate_link()

    return Response({"status": "OK", "check_link": link}, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def check_link(request):
    global val
    val += 1
    # breakpoint()
    # check
    if val % 3 == 0:
        return Response({"status": "OK", "pay_link": "http://localhost:8000/pay/check_link", "check": val, "id": request.query_params['id']}, status=status.HTTP_200_OK)
    return Response(
        {"status": "PENDING", "check": val, "id": request.query_params['id']},
        status=status.HTTP_202_ACCEPTED
    )


@api_view(['GET'])
def check_status(request):
    global val
    val += 1
    if val % 3 == 0:
        return Response({"status": "OK"}, status=status.HTTP_200_OK)

    return Response({"status": "PENDING"}, status=status.HTTP_202_ACCEPTED)