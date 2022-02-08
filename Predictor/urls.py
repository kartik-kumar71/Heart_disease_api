from django.urls import path
from .views import *

urlpatterns = [
    path('classify/', ml_model.as_view(), name = 'prediction'),
]