from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import NetworkNode

from .serializers import NetworkNodeSerializer, UpdateNetworkNodeSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = NetworkNode.objects.all()
    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
        'contact__country': ['exact', 'icontains'],  # точное совпадение или частичное
    }

    def get_serializer_class(self):
        if self.action in ["update", "retrieve"]:
            return UpdateNetworkNodeSerializer
        else:
            return NetworkNodeSerializer
