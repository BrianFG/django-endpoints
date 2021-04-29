from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .helpers.text_number_lib import number_to_words


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        number = request.query_params.get('number', None)
        if number:
            try:
                number = int(number)
                return Response(" ".join(number_to_words(number)))
            except ValueError:
                message = {
                    "status": "failed",
                    "error_message": f"Value '{number}' is not a number"
                }
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

