
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
from .ml_model import predict_churn
from .models import ChurnPrediction
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def predict_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            features = [
                float(data['feature1']), float(data['feature2']), float(data['feature3']),
                float(data['feature4']), float(data['feature5']), float(data['feature6']),
                float(data['feature7']), float(data['feature8'])
            ]
            
            churn_probability = predict_churn(features)

            # Save prediction to database
            prediction = ChurnPrediction.objects.create(
                feature1=features[0], feature2=features[1], feature3=features[2],
                feature4=features[3], feature5=features[4], feature6=features[5],
                feature7=features[6], feature8=features[7],
                churn_probability=churn_probability
            )
            
            return JsonResponse({"churn_probability": churn_probability}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)
