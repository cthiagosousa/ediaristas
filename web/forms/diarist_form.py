from django.forms import ModelForm, CharField, TextInput
from ..models import Diarist

class DiaristForm(ModelForm):
    cpf = CharField(widget=TextInput(attrs={'data-mask':"000.000.000-00"}))
    cep = CharField(widget=TextInput(attrs={'data-mask':"0000-000"}))
    telefone = CharField(widget=TextInput(attrs={'data-mask': "(00) 00000-0000"}))

    class Meta:
        model = Diarist
        fields = '__all__'
    
    def cleanCpf(self):
        cpf = self.cleaned_data['cpf']
        return cpf.replace('.', '').replace('-', '')
    
    def cleanCep(self):
        cep = self.cleaned_data['cep']
        return cep.replace('-', '')
    
    def cleanTelefone(self):
        telefone = self.cleaned_data['telefone']
        return telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
