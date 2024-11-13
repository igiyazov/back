import random
import string

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.payment.utils import generate_link

val = 0
method = ''


@api_view(['GET'])
def get_link(request):
    global method
    method = request.query_params.get("method")
    link = generate_link()

    return Response({"status": 1, "check_link": link}, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def check_link(request):
    global val
    val += 1
    if val % 10 == 0:
        return Response({"status": 2, "pay_link": f"/pay/check_link/{method}", "check": val, "id": request.query_params['id']}, status=status.HTTP_200_OK)
    return Response(
        {"status": 3, "check": val, "id": request.query_params['id']},
        status=status.HTTP_202_ACCEPTED
    )


@api_view(['GET'])
def check_status(request):
    global val
    val += 1
    if val % 5 == 0:
        return Response({"status": 4}, status=status.HTTP_200_OK)

    return Response({"status": 5}, status=status.HTTP_202_ACCEPTED)
