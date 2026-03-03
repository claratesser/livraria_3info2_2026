from rest_framework.viewsets import ModelViewSet

from core.models import Editora
from core.serializers import EditoraSerializer


class EditoraViewset(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer