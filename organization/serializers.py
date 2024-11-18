from rest_framework import serializers
from .models import Department, Position, Employee, PermissionGroup

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'parent']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name', 'description']

class PermissionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionGroup
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True)
    positions = PositionSerializer(many=True)

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'departments', 'positions']