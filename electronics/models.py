from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода на рынок')

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class TradingNetwork(models.Model):
    # Уровни иерархии
    LEVEL_FACTORY = 0
    LEVEL_RETAIL = 1
    LEVEL_ENTREPRENEUR = 2

    LEVEL_CHOICES = [
        (LEVEL_FACTORY, 'Завод'),
        (LEVEL_RETAIL, 'Розничная сеть'),
        (LEVEL_ENTREPRENEUR, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255, verbose_name='Название')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Уровень')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    # Ссылка на поставщика (предыдущее звено). Может быть пустым для Завода.
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Поставщик',
        related_name='children'
    )

    # Продукты: связь "Многие-ко-Многим"
    products = models.ManyToManyField(Product, verbose_name='Продукты')

    # Задолженность (нельзя обновлять через API)
    debt_to_supplier = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name='Задолженность перед поставщиком'
    )

    # Время создания (автоматически)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Звено торговой сети'
        verbose_name_plural = 'Звенья торговой сети'

