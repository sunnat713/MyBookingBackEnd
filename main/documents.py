from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Restaurant, RestaurantCategory, RestaurantMenu

@registry.register_document
class RestaurantDoc(Document):
    class Index:
        name = "Restaurants"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = Restaurant
        fields = [
            'id',
            'name',
            'location'
        ]