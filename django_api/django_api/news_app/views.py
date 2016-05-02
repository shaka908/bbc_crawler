from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import ParseError

from pymongo import MongoClient
import re

# from models import News
# from serializers import NewsSerializer


MONGO_URL = 'mongodb://test_ivan:11111111@aws-us-east-1-portal \
    .11.dblayer.com:27790,aws-us-east-1-portal.10.dblayer.com:11140/bbc'

client = MongoClient(MONGO_URL)
db = client['bbc']
coll = db['news']

class SearchOrViewSet(viewsets.ViewSet):
    def list(self, request):
        records = coll.find({}, {'_id':0}, limit=10)
        result = [x for x in records]
        return Response(result)

    def retrieve(self, request, pk=None):
        records = coll.find(
            {'$text':{'$search':pk}},
            {'_id':0},
            limit = 50
        )
        result = [x for x in records]
        return Response(result)

class SearchAndViewSet(viewsets.ViewSet):
    def list(self, request):
        records = coll.find({}, {'_id':0}, limit=10)
        result = [x for x in records]
        return Response(result)

    def retrieve(self, request, pk=None):
        records = coll.find(
            {'$text':{'$search':'\"' + pk + '\"'}},
            {'_id':0},
            limit = 50
        )
        result = [x for x in records]
        return Response(result)


class LookupUrlViewSet(viewsets.ViewSet):
    def list(self, request):
        records = coll.find({}, {'_id':0}, limit=10)
        result = [x for x in records]
        return Response(result)

    def retrieve(self, request, pk=None):
        url_base = 'http://www.bbc.com/news/'
        records = coll.find(
            {'url': url_base + pk},
            {'_id':0},
            limit = 50
        )
        result = [x for x in records]
        return Response(result)

class LookupDateViewSet(viewsets.ViewSet):
    def list(self, request):
        records = coll.find({}, {'_id':0}, limit=10)
        result = [x for x in records]
        return Response(result)

    def retrieve(self, request, pk=None):
        dt_tamp = r'^\d{1,2}\s\w{3,9}\s\d{4}$'
        # print '__' + pk + '__'
        if re.match(dt_tamp, pk):
            records = coll.find(
                {'datetime': pk},
                {'_id':0},
                limit = 50
            )
            result = [x for x in records]
            return Response(result)
        else:
            raise ParseError('Date must be dd month year format.')
