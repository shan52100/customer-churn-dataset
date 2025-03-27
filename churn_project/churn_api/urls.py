from django.urls import path
from .views import *

urlpatterns = [
    path('predict/', predict_view, name='predict_churn'),
    path('home/', home, name='home'),
]