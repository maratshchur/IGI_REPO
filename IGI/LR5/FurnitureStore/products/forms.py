from datetime import datetime, timedelta
from django import forms
from.models import Order, ProductType, Promocode, PickupPoint, Product

class PaymentForm(forms.Form):
    pickup_location = forms.ModelChoiceField(queryset=PickupPoint.objects.all(), required=True)
    promo_code = forms.CharField(max_length=20, required=False)
    
class OrderForm(forms.ModelForm):
    quantity = forms.IntegerField(label='Количество', min_value=1)
    promocode = forms.CharField(label='Промокод', required=False)

    class Meta:
        model = Order
        fields = ('product', 'quantity', 'pickup_point', 'promocode')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()
        self.fields['pickup_point'].queryset = PickupPoint.objects.all()
        
        
    def clean_promocode(self):
        promocode_code = self.cleaned_data['promocode']
        if promocode_code and not Promocode.objects.filter(code=promocode_code, is_active=True).exists():
            raise forms.ValidationError('Промокод не существует или не активен')
        return promocode_code

    def save(self, commit=True):
        order = super().save(commit=False)
        product = order.product
        production_time = product.production_time*order.quantity
        current_date = datetime.now().date()
        completion_date = current_date + timedelta(days=production_time)
        order.date = current_date
        order.completion_date = completion_date
        promocode_code = self.cleaned_data['promocode']
        if promocode_code:
            try:
                promocode = Promocode.objects.get(code=promocode_code, is_active=True)
                # Apply the promocode discount to the revenue
                discount_percentage = promocode.discount
                order.revenue = order.product.price * order.quantity * (1 - discount_percentage / 100)
            except Promocode.DoesNotExist:
                # If the promocode is not valid, use the original price
                order.revenue = order.product.price * order.quantity
        else:
            # If no promocode is entered, use the original price
            order.revenue = order.product.price * order.quantity

        if commit:
            order.save()
        return order    
    
    
class ProductForm(forms.ModelForm):
    pickup_points = forms.ModelMultipleChoiceField(
        queryset=PickupPoint.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Точки самовывоза'
    )

    class Meta:
        model = Product
        fields = ('name', 'code', 'product_type', 'model', 'price', 'production_time', 'image', 'pickup_points', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_type'].empty_label = 'Выберите вид изделия'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        code = cleaned_data.get('code')
        if Product.objects.filter(name=name, code=code).exists():
            raise forms.ValidationError('Продукт с таким наименованием и кодом уже существует')
        return cleaned_data
        
from django.core.validators import MaxValueValidator

class PromoCodeForm(forms.ModelForm):
    discount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MaxValueValidator(100)],
        help_text='Максимальная скидка 100%', 
        label='Скидка'
    )

    class Meta:
        model = Promocode
        fields = ('name', 'description', 'code', 'discount', 'is_active')
        
        
    def clean_promocode_code(self):
        promocode_code = self.cleaned_data['promocode_code']
        if not Promocode.objects.filter(code=promocode_code, is_active=True).exists():
            raise forms.ValidationError('Промокод не существует или не активен')
        return promocode_code


class PickupPointForm(forms.ModelForm):
    class Meta:
        model = PickupPoint
        fields = ('name', 'address')
             

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Вид изделия'