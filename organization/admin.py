from django.contrib import admin
from .models import Department, Position, Employee, PermissionGroup

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(PermissionGroup)