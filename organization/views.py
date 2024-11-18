from rest_framework import viewsets
from .models import Department, Position, Employee, PermissionGroup
from .serializers import DepartmentSerializer, PositionSerializer, EmployeeSerializer, PermissionGroupSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PermissionGroupViewSet(viewsets.ModelViewSet):
    queryset = PermissionGroup.objects.all()
    serializer_class = PermissionGroupSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
