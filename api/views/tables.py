from rest_framework import viewsets
from api.models.tables import Table
from api.serializers.tables import TableSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer