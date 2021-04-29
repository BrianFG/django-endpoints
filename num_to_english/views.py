from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .helpers.text_number_lib import number_to_words


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        return Response(" ".join(number_to_words(12345678)))

