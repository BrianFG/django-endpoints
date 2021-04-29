from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .helpers.text_number_lib import number_to_words


@api_view(['GET', 'POST'])
def index(request):
    number = None
    if request.method == 'GET':
        number = request.query_params.get('number', None)
    if request.method == 'POST':
        number = request.data.get('number', None)
    if number is not None:
        try:
            number = int(number)
            text_number = " ".join(number_to_words(number))
            message = {
                "status": "ok",
                "num_to_english": text_number
            }
            return Response(message)
        except ValueError:
            message = {
                "err": True,
                "status": "failed",
                "error_message": f"Value '{number}' is not a number"
            }
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    message = {
        "err": True,
        "status": "failed",
        "message": "Server error"
    }
    return Response(message, status=status.HTTP_501_NOT_IMPLEMENTED)



