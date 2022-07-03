from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):

    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)
    
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permission())
    #     if user.is_staff:
    #        return True
    #     return False

    # def has_object_permission(self, request, view, obj):
    #     return obj.owner == request.user