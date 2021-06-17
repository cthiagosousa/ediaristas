from rest_framework.views import APIView
from .services.get_cep_service import listDiaristsByCity
from .serializers.diarist_city_serializer import DiaristCitySerializer
from ediaristas.api.pagination.diarist_pagination import DiaristPagination

class DiaristView(APIView, DiaristPagination):
    def get(self, request, format=None):
        cep = self.request.query_params.get("cep", None)
        diarists = listDiaristsByCity(cep)
        result = self.paginate_queryset(diarists, request)
        serializer = DiaristCitySerializer(result, many=True, context={'request': request})
        
        return self.get_paginated_response(serializer)
