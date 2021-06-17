from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class DiaristPagination(PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):

        return Response({
            "quantidade_diaristas": self.page.count - self.page_size,
            "diaristas": data,
        })
