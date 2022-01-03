from rest_framework import fields, serializers
from .models import Random_Quotes

class Key(serializers.ModelSerializer):
    class Meta:
        model = Random_Quotes
        fields = ['id', 'Quote', 'Author']
         