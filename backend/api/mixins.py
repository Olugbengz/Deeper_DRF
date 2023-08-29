from rest_framework import permissions 
from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMisin():
    permission_classes = [permissions.IsAdminUser, 
    IsStaffEditorPermission]