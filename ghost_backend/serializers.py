from rest_framework.serializers import HyperlinkedModelSerializer
from ghost_backend.models import Boast


class BoastSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Boast
        fields = [
            'boast',
            'message',
            'post_time',
            'total_votes',
            'secret_code',
            'id'
        ]
