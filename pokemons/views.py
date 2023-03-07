from django.shortcuts import render

# Create your views here.
import requests
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Digimon
from .serializers import DigimonSerializer

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class PokemonTotalDataView(View):
    def get(self, request, *args, **kwargs):
        url = 'https://digimon-api.vercel.app/api/digimon'
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data ,safe=False)
    


class AddToFavoriteView(APIView):
    def post(self, request):
        serializer = DigimonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DigimonListView(ListCreateAPIView):
    queryset = Digimon.objects.all()
    serializer_class = DigimonSerializer

class DigimonDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Digimon.objects.all()
    serializer_class= DigimonSerializer