from rest_framework import generics
from .models import idea
from .serializers import ideaSerializer
from django.shortcuts import get_object_or_404

class ideaList(generics.ListCreateAPIView):
    queryset=idea.objects.all()
    serializer_class=ideaSerializer
    
    def get_object(self):
        queryset=self.get_queryset()
        obj =get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj