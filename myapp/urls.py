from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView),
    path('creditsave/',CreditSaveView),
    path('debitsave/',DebitSaveView),
    path('transfersave/',TransferSaveView),
    path('generatefastbtn/',GenerateFastButtonView),
    path('fastbtn/',FastButtonView),
]
