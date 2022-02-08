from django.apps import AppConfig

from django.conf import settings
import joblib

import os

class PredictorConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    name = 'Predictor'
    MODEL_FILE = os.path.join(settings.MODEL, 'heart_failure_model.joblib')
    RF = joblib.load(MODEL_FILE)
