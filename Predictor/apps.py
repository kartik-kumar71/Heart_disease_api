from django.apps import AppConfig
import os

from django.conf import settings
import pickle


class PredictorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Predictor'
    MODEL_FILE = os.path.join(settings.MODEL, 'heart_failure_model.sav')
    RF = pickle.load(open(MODEL_FILE,'rb'))
