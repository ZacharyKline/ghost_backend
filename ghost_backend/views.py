from rest_framework import viewsets
from ghost_backend import models, serializers
from rest_framework.response import Response
from rest_framework.decorators import action


class BoastViewSet(viewsets.ModelViewSet):
    queryset = models.Boast.objects.all()
    serializer_class = serializers.BoastSerializer

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        like = models.Boast.objects.get(pk=pk)
        like.total_votes += 1
        like.save()
        return Response({'status': 'liked!'})

    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        like = models.Boast.objects.get(pk=pk)
        like.total_votes -= 1
        like.save()
        return Response({'status': 'unliked!'})
