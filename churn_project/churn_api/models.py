from django.db import models

class ChurnPrediction(models.Model):
    feature1 = models.FloatField()
    feature2 = models.FloatField()
    feature3 = models.FloatField()
    feature4 = models.FloatField()
    feature5 = models.FloatField()
    feature6 = models.FloatField()
    feature7 = models.FloatField()
    feature8 = models.FloatField()
    churn_probability = models.FloatField()
    predicted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction at {self.predicted_at} - Churn: {self.churn_probability:.2f}"
