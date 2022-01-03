from django.db import models
from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .models import Random_Quotes
from .serializers import Key
from rest_framework.views import APIView
# Create your views here.

'''class QuotesList(generics.ListCreateAPIView):
    main = Random_Quotes.objects.all()
    serializer_class = Key

class QuotesDetails(generics.RetrieveUpdateDestroyAPIView):
    main = Random_Quotes.objects.all()
    serializer_class = Key

#class QuotesCreate(generics.CreateAPIView):
#    def get():
#        main = Random_Quotes.objects.all()
#        serializer_class = Key
#    def post(id, quote):
        
'''


class QuotesList(APIView):
    def get(self, request):
        qoute = Random_Quotes.objects.all()
        serialized_quote = Key(qoute, many=True)
        return JsonResponse(serialized_quote.data, safe=False)

    def post(self, request):
        quotes = Random_Quotes
        quote_data = Key(data=request.data)
        if quote_data.is_valid():
            quote_data.save()
            return JsonResponse(quote_data.data, safe=False)
        return JsonResponse(quote_data.errors, safe=False, status=400)


class QuotesGet(APIView):
    def get_id(self, id):
        try:
            return Random_Quotes.objects.get(id=id)
        except Random_Quotes.DoesNotExist:
            return Http404

    def put(self, request, id, format=None):
        id_gotten = self.get_id(id)
        quote = Random_Quotes.objects.all()
        modified_data = Key(id_gotten, data=request.data)
        if modified_data.is_valid():
            modified_data.save()
            return JsonResponse(modified_data.data, safe=False)
        return JsonResponse(modified_data.errors, safe=False)

    def get(self, request, id, format=None):
        id_gotten = self.get_id(id)
        serialized_quote = Key(id_gotten)
        return JsonResponse(serialized_quote.data, safe=False)

    def delete(self, request, id, format=None):
        id_gotten = self.get_id(id)
        id_gotten.delete()
        return JsonResponse('Delete Succesful!', safe=False)
