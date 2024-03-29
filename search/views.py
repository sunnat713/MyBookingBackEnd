import abc
from main.serializers import RestaurantSerializer
from main.documents import RestaurantDoc
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from elasticsearch_dsl import Q
from django.http import HttpResponse
from .serialziers.restaurant import RestaurantDocumentSerializer
# Create your views here.

class PaginatedElasticSearchAPIView(APIView, PageNumberPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()
            
            # print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)

            return self.get_paginated_response(serializer.data)            
        except Exception as e:
            return HttpResponse(e, status=500)
            


class SearchRestaurant(PaginatedElasticSearchAPIView):
    serializer_class = RestaurantSerializer
    document_class = RestaurantDoc

    def generate_q_expression(self, query):
        return Q(
            'multi_match', query=query,
            fields=[
                'name',
            ], fuzziness='auto') #fuzziness=auto  djengo ==> django suggestion
    
    # def generate_q_expression(self, query):
    #     return Q('bool',
    #             should=[
    #                 Q('match', name=query)
    #             ], minimum_should_match=1)

