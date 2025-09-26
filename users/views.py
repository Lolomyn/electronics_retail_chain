from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import Employee
from users.serializers import CreateEmployeeSerializer


class EmployeeCreateAPIView(CreateAPIView):
    serializer_class = CreateEmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        employee = serializer.save(is_active=True)
        employee.set_password(employee.password)
        employee.save()
