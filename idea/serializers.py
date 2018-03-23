from .models import idea
from rest_framework import serializers

class ideaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=idea
        fields=('title','description','created_at')
