from django.urls import path
from .views import DiaristView

urlpatterns = [
    path('diarist-city', DiaristView.as_view(), name='diarist-city')
]
