from curses import ACS_GEQUAL
from django.shortcuts import render

from .apps import PredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView

class ml_model(APIView):
    def get(self,request):
        if request.method == 'GET':

            Age = request.GET.get('Age')
            RestingBP = request.GET.get('RestingBP')
            Cholesterol = request.GET.get('Cholesterol')
            FastingBS = request.GET.get('FastingBS')
            MaxHR = request.GET.get('MaxHR')
            Oldpeak = request.GET.get('Oldpeak')
            Sex = request.GET.get('Sex')
            ChestPainType = request.GET.get('ChestPainType')
            RestingECG = request.GET.get('RestingECG')
            ExerciseAngina = request.GET.get('ExerciseAngina')
            ST_Slope = request.GET.get('ST_Slope')

            return JsonResponse({})
