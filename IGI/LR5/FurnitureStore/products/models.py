from django.db import models
from users.models import Customer

class ProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Вид изделия')

    class Meta:
        verbose_name = 'Тип мебели'
        verbose_name_plural = 'Типы мебели'
        
    def __str__(self):
        return self.name

class PickupPoint(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование точки самовывоза')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Точка самовывоза'
        verbose_name_plural = 'Точки самовывоза'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    code = models.IntegerField(verbose_name='Код продукта')
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='Вид изделия')
    model = models.CharField(max_length=50, verbose_name='Модель')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    production_time = models.IntegerField(verbose_name='Время изготовления')
    image = models.ImageField(upload_to='images/', verbose_name='Картинка')
    pickup_points = models.ManyToManyField(PickupPoint, verbose_name='Точки самовывоза')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
    def __str__(self):
        return self.name
    
    
        
class Order(models.Model):
    date = models.DateField(verbose_name='Дата заказа')
    completion_date = models.DateField(verbose_name='Дата выполнения заказа')
    client = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.IntegerField(verbose_name='Количество')
    pickup_point = models.ForeignKey(PickupPoint, on_delete=models.CASCADE, verbose_name='Точка самовывоза')
    promocode = models.CharField(max_length=20,verbose_name="Промокод",blank=True)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Выручка")
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        
    def __str__(self):
        return f'Заказ {self.product.name} от {self.date}'

    

class Promocode(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название промокода')
    description = models.TextField(verbose_name='Описание промокода')
    code = models.CharField(max_length=255, verbose_name='Код промокода')
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Скидка')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    
    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'

    def __str__(self):
        return self.code
    


class Cart(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элемент корзины'

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"