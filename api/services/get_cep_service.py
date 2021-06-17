import json

from rest_framework.serializers import ValidationError
from web.services.cep_service import searchCityCep
from web.models import Diarist

def listDiaristsByCity(cep):
    ibge_code = getCityByCep(cep)["ibge"]
    diarists = Diarist.objects.filter(codigo_ibge = ibge_code).order_by("id")

    return diarists

def getCityByCep(cep):
    response = searchCityCep(cep)

    if response.status_code == 400:
        raise ValidationError('O CEP informado é invalido.')

    response_json = json.loads(response.content)

    if 'erro' in response_json:
        raise ValidationError('O CEP informado não foi encontrado')
    
    return  response_json
