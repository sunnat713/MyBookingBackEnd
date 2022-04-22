import json
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Restaurant, RestaurantCategory, RestaurantMenu


@registry.register_document
class RestaurantDoc(Document):
    category = fields.ObjectField(properties={
        'pk': fields.IntegerField(),
    })
    user = fields.ObjectField(properties={
        "pk": fields.IntegerField()
    })
    logo = fields.FileField()
    location = fields.TextField()
    
    class Index:
        name = "restaurants"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = Restaurant
        fields = [
            'id',
            'name'
        ]
    
    # def prepare_logo(self, instance):
    
    #     print(instance.logo,"INSTANCE===============")
    #     return instance.logo if instance.logo else None