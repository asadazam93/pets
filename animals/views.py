from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from animals.serializers import CatSerializer, DogSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class DogViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = DogSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        return self.request.user.dogs.all()


class CatViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = CatSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        return self.request.user.cats.all()


