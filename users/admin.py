from django.contrib import admin

from users.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name", "is_active")
    list_filter = ("username",)
    search_fields = ("username",)
