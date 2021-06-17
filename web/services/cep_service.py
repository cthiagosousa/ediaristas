import requests

def searchCityCep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    return response
