import json

from django.http import HttpResponse
from rest_framework.views import APIView

from .util import fizz_buzz

class FizzBuzzView(APIView):

    def get(self, request, since=1, until=100, format=None):
        values = fizz_buzz(since, until)
        return HttpResponse(json.dumps(values), content_type='application/json')
