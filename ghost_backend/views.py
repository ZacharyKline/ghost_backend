from rest_framework import viewsets
from ghost_backend import models, serializers


class BoastViewSet(viewsets.ModelViewSet):
    queryset = models.Boast.objects.all()
    serializer_class = serializers.BoastSerializer
