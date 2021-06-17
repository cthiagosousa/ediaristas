import json

from django.forms import ModelForm, CharField, TextInput, ValidationError
from ..models import Diarist
from ..services import cep_service

class DiaristForm(ModelForm):
    cpf = CharField(widget=TextInput(attrs={'data-mask':"000.000.000-00"}))
    cep = CharField(widget=TextInput(attrs={'data-mask':"0000-000"}))
    telefone = CharField(widget=TextInput(attrs={'data-mask': "(00) 00000-0000"}))
    # codigo_ibge = IntegerField(required=False)

    class Meta:
        model = Diarist
        exclude = ('codigo_ibge',)
    
    def cleanCpf(self):
        cpf = self.cleaned_data['cpf']
        return cpf.replace('.', '').replace('-', '')
    
    def cleanCep(self):
        cep = self.cleaned_data['cep']
        formatted_cep = cep.replace('-', '')
        response = cep_service.searchCityCep(formatted_cep)

        if response.status_code == 400:
            raise ValidationError('O CEP informado é invalido.')

        response_json = json.loads(response.content)

        if 'error' in response_json:
            raise ValidationError('O CEP informado não foi encontrado')

        return formatted_cep
    
    def cleanTelefone(self):
        telefone = self.cleaned_data['telefone']
        return telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')

    def save(self, commit=True):
        instance = super(DiaristForm, self).save(commit=False)
        response = cep_service.searchCityCep(self.cleaned_data.get('cep'))
        response_json = json.loads(response.content)
        instance.codigo_ibge = response_json['ibge']
        instance.save()

        return instance