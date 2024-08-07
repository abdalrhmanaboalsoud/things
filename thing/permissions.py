from rest_framework import permissions

import logging

logger = logging.getLogger(__name__)

class IsOwnerOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """
    message = 'You must be the owner of this object to perform any action.'

    def has_object_permission(self, request, view, obj):
        logger.debug(f"User: {request.user}, Owner: {obj.owner}")
        if request.user == obj.owner:
            return True
        return False
