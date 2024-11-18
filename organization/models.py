from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subdepartments')
    
    def __str__(self):
        return self.name
    
class PermissionGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    permission_group = models.ForeignKey(PermissionGroup, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    departments = models.ManyToManyField(Department, related_name='employees')
    positions = models.ManyToManyField(Position, related_name='employees')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'
    



