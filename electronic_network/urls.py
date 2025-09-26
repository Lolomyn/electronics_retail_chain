from django.urls import path

from electronic_network.apps import ElectronicNetworkConfig
from electronic_network.views import NetworkNodeViewSet

app_name = ElectronicNetworkConfig.name

urlpatterns = [
    path(
        "networks/create/",
        NetworkNodeViewSet.as_view({"post": "create"}),
        name="network-create",
    ),
    path("networks/", NetworkNodeViewSet.as_view({"get": "list"}), name="network-list"),
    path(
        "networks/<int:pk>/",
        NetworkNodeViewSet.as_view({"get": "retrieve"}),
        name="network-list",
    ),
    path(
        "networks/<int:pk>/update/",
        NetworkNodeViewSet.as_view({"put": "update", "patch": "update"}),
        name="network-update",
    ),
    path(
        "networks/<int:pk>/delete/",
        NetworkNodeViewSet.as_view({"delete": "destroy"}),
        name="network-delete",
    ),
]
