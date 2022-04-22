import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from main.documents import RestaurantDoc

class RestaurantDocumentSerializer(DocumentSerializer):
    """Serializer for the Restaurant document."""
    logo = serializers.ImageField(read_only=True)
    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = RestaurantDoc

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = "__all__"