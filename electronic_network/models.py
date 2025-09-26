from django.db import models


class Contact(models.Model):
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=20, verbose_name="Номер дома")

    def __str__(self):
        return f"{self.country} г. {self.city} ул. {self.street}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class NetworkNode(models.Model):
    NODE_TYPE_CHOICES = (
        ("factory", "Завод"),
        ("retail_network", "Розничная сеть"),
        ("individual_entrepreneur", "Индивидуальный предприниматель"),
    )

    name = models.CharField(max_length=255, verbose_name="Название")
    node_type = models.CharField(
        max_length=25, choices=NODE_TYPE_CHOICES, verbose_name="Тип звена"
    )
    contact = models.OneToOneField(
        Contact, on_delete=models.CASCADE, verbose_name="Контакты"
    )
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    supplier = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Поставщик",
        related_name="children",
    )
    debt = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
        verbose_name="Задолженность перед поставщиком",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"

    @property
    def hierarchy_level(self):
        """Динамическое вычисление уровня иерархии"""
        if self.supplier is None:
            return 0
        return self.supplier.hierarchy_level + 1
