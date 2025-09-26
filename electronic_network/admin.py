from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html

from electronic_network.models import Contact, NetworkNode, Product


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "country", "city", "street", "house_number")
    list_filter = ("email",)
    search_fields = ("email",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "model", "release_date")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "node_type",
        "get_contact_info",
        "get_products_list",
        "supplier_link",
        "debt",
        "created_at",
        "is_active",
    )

    list_filter = ("name", "contact__city")
    search_fields = ("name", "contact__city")
    actions = ["clear_debt_action"]

    def supplier_link(self, obj):
        """Ссылка на поставщика"""
        if obj.supplier:
            url = reverse(
                "admin:electronic_network_networknode_change", args=[obj.supplier.id]
            )
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return "-"

    supplier_link.short_description = "Поставщик"

    def get_products_list(self, obj):
        """Отображает список продуктов через запятую"""
        return ", ".join([product.name for product in obj.products.all()])

    get_products_list.short_description = "Продукты"

    def get_contact_info(self, obj):
        """Отображает email из контактов"""
        return (
            f"[{obj.contact.email}] --- {obj.contact.country}, г. {obj.contact.city}, "
            f"ул. {obj.contact.street}, д. {obj.contact.house_number}"
        )

    get_contact_info.short_description = "Контакты"

    def clear_debt_action(self, request, queryset):
        """Admin action для очистки задолженности"""
        updated_count = queryset.update(debt=0)

        # Сообщение об успехе
        self.message_user(
            request,
            f"Задолженность очищена у {updated_count} объектов",
            messages.SUCCESS,
        )

    clear_debt_action.short_description = "Очистить задолженность перед поставщиком"
