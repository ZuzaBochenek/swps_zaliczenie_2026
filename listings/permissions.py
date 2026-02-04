from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Pozwala na odczyt wszystkim,
    zapis tylko właścicielowi obiektu.
    """

    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS → dozwolone
        if request.method in SAFE_METHODS:
            return True

        # PUT, PATCH, DELETE → tylko właściciel
        return obj.owner == request.user
