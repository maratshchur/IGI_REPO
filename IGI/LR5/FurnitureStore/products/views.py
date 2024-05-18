import datetime
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from products.admin_dashboard import build_product_popularity, calculate_linear_trend, get_city_customers, get_monthly_sales, make_sales_forecast, plot_sales_data
from .forms import OrderForm, PickupPointForm, ProductForm, ProductTypeForm, PromoCodeForm
from .models import Product, Customer, Order, Promocode, PickupPoint, ProductType
import matplotlib.pyplot as plt
from django.db.models.functions import TruncMonth
from .month_names import MONTH_NAMES

import logging
import calendar
import datetime
logger = logging.getLogger('db_logger')

def home(request):
    logger.info('Home page accessed')
    c = calendar.TextCalendar()
    d = datetime.date.today()
    s = c.formatmonth(d.year, d.month)
    
    products = Product.objects.all()
    product_types = ProductType.objects.values_list('name', flat=True).distinct()
    
    return render(request, 'products/home.html', {
        'products': products,
        'product_types': product_types,
        'calendar': s
    })

def product_detail(request, pk):
    logger.info(f'Product detail page accessed for product {pk}')
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def search_products(request):
    logger.info('Search products page accessed')
    q = request.GET.get('q')
    products = Product.objects.filter(name__icontains=q)
    product_types = ProductType.objects.values_list('name', flat=True).distinct()
    return render(request, 'products/home.html', {'products': products, 'product_types': product_types})

def filter_products(request):
    logger.info('Filter products page accessed')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    product_types = request.GET.get('product_type')

    products = Product.objects.all()

    if product_types:
        product_type_id = ProductType.objects.get(name=product_types).id
        products = Product.objects.filter(price__gte=price_min, price__lte=price_max, product_type_id=product_type_id)
    else:
        products = Product.objects.filter(price__gte=price_min, price__lte=price_max)

    product_types = ProductType.objects.values_list('name', flat=True).distinct()
    return render(request, 'products/home.html', {'products': products, 'product_types': product_types})

@login_required
def price_list(request):
    logger.info('Price list page accessed')
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    product_types = ProductType.objects.all()
    products = Product.objects.all()
    return render(request, 'products/price_list.html', {'product_types': product_types, 'products': products})

@login_required
def customer_list(request):
    logger.info('Customer list page accessed')
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    customers = Customer.objects.all()
    cities = customers.values_list('city', flat=True).distinct()
    customer_list = []
    for city in cities:
        city_customers = customers.filter(city=city)
        customer_list.append((city, city_customers))
    return render(request, 'products/customer_list.html', {'customer_list': customer_list})

@login_required
def create_order(request, product_id):
    logger.info(f'Create order page accessed for product {product_id}')
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.client = request.user.customer
            order.save()
            logger.info(f'Order created for product {product_id}')
            return redirect('home')
    else:
        order_form = OrderForm()
    return render(request, 'products/create_order.html', {'order_form': order_form})

@login_required
def user_orders(request):
    logger.info('User orders page accessed')
    orders = Order.objects.filter(client=request.user.customer)
    return render(request, 'products/customer_orders.html', {'orders': orders})

@login_required
def promo_codes(request):
    logger.info('Promo codes page accessed')
    promo_codes = Promocode.objects.all()
    return render(request, 'products/promo_codes.html', {'promo_codes': promo_codes})

@login_required
def pickup_points(request):
    logger.info('Pickup points page accessed')
    pickup_points = PickupPoint.objects.all()
    return render(request, 'products/pickup_points.html', {'pickup_points': pickup_points})

@login_required
def employee_dashboard(request):
    logger.info('Employee dashboard page accessed')
    if not request.user.is_staff:
        return HttpResponseForbidden()

    orders = Order.objects.all()
    wholesalers = Customer.objects.all()

    context = {
        'orders': orders,
        'wholesalers': wholesalers
    }

    return render(request, 'products/employee_dashboard.html', context)

def create_product(request):
    logger.info('Create product page accessed')
    if not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            logger.info('Product created')
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'products/create_product.html', {'form': form})

@login_required
def pickup_points_list(request):
    logger.info('Pickup points list page accessed')
    pickup_points = PickupPoint.objects.all()
    return render(request, 'products/pickup_points_list.html', {'pickup_points': pickup_points})

@login_required
def create_pickup_point(request):
    logger.info('Create pickup point page accessed')
    if not request.user.is_superuser:
        return redirect('pickup_points_list')

    if request.method == 'POST':
        form = PickupPointForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Pickup point created')
            return redirect('pickup_points_list')
    else:
        form = PickupPointForm()

    return render(request, 'products/create_pickup_point.html', {'form': form})

@login_required
def update_pickup_point(request, pk):
    logger.info(f'Update pickup point page accessed for pickup point {pk}')
    pickup_point = PickupPoint.objects.get(pk=pk)
    if not request.user.is_superuser:
        return redirect('pickup_points_list')

    if request.method == 'POST':
        form = PickupPointForm(request.POST, instance=pickup_point)
        if form.is_valid():
            form.save()
            logger.info(f'Pickup point {pk} updated')
            return redirect('pickup_points_list')
    else:
        form = PickupPointForm(instance=pickup_point)

    return render(request, 'products/update_pickup_point.html', {'form': form, 'pickup_point': pickup_point})

@login_required
def delete_pickup_point(request, pk):
    logger.info(f'Delete pickup point page accessed for pickup point {pk}')
    pickup_point = PickupPoint.objects.get(pk=pk)
    if not request.user.is_superuser:
        return redirect('pickup_points_list')

    if request.method == 'POST':
        pickup_point.delete()
        logger.info(f'Pickup point {pk} deleted')
        return redirect('pickup_points_list')

    return render(request, 'products/delete_pickup_point.html', {'pickup_point': pickup_point})


@login_required
def promo_codes_list(request):
    logger.info('Promo codes list page accessed')
    promo_codes = Promocode.objects.all()
    return render(request, 'products/promo_codes.html', {'promo_codes': promo_codes})

@login_required
def create_promocode(request):
    logger.info('Create promo code page accessed')
    if not request.user.is_superuser:
        return redirect('promo_codes')

    if request.method == 'POST':
        form = PromoCodeForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Promo code created')
            return redirect('promo_codes')
    else:
        form = PromoCodeForm()

    return render(request, 'products/create_promocode.html', {'form': form})

@login_required
def update_promocode(request, pk):
    logger.info(f'Update promo code page accessed for promo code {pk}')
    promo_code = Promocode.objects.get(pk=pk)
    if not request.user.is_superuser:
        return redirect('promo_codes')

    if request.method == 'POST':
        form = PromoCodeForm(request.POST, instance=promo_code)
        if form.is_valid():
            form.save()
            logger.info(f'Promo code {pk} updated')
            return redirect('promo_codes')
    else:
        form = PromoCodeForm(instance=promo_code)

    return render(request, 'products/promocode_update.html', {'form': form, 'promo_code': promo_code})

@login_required
def delete_promocode(request, pk):
    logger.info(f'Delete promo code page accessed for promo code {pk}')
    promo_code = Promocode.objects.get(pk=pk)
    if not request.user.is_superuser:
        return redirect('promo_codes')

    if request.method == 'POST':
        promo_code.delete()
        logger.info(f'Promo code {pk} deleted')
        return redirect('promo_codes')

    return render(request, 'products/delete_promocode.html', {'promo_code': promo_code})

@login_required
def product_types_list(request):
    logger.info('Product types list page accessed')
    product_types = ProductType.objects.all()
    return render(request, 'products/product_types_list.html', {'product_types': product_types})

@login_required
def create_product_type(request):
    logger.info('Create product type page accessed')
    if not request.user.is_superuser:
        return redirect('product_types_list')

    if request.method == 'POST':
        form = ProductTypeForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Product type created')
            return redirect('product_types_list')
    else:
        form = ProductTypeForm()

    return render(request, 'products/create_product_type.html', {'form': form})

@login_required
def update_product_type(request, pk):
    logger.info(f'Update product type page accessed for product type {pk}')
    product_type = ProductType.objects.get(pk=pk)
    if not request.user.is_superuser:
        return redirect('product_types_list')

    if request.method == 'POST':
        form = ProductTypeForm(request.POST, instance=product_type)
        if form.is_valid():
            form.save()
            logger.info(f'Product type {pk} updated')
            return redirect('product_types_list')
    else:
        form = ProductTypeForm(instance=product_type)

    return render(request, 'products/update_product_type.html', {'form': form, 'product_type': product_type})

@login_required
def delete_product_type(request, pk):
    logger.info(f'Delete product type page accessed for product type {pk}')
    product_type = ProductType.objects.get(pk=pk)
    if not request.user.is_superuser:
        return redirect('product_types_list')

    if request.method == 'POST':
        product_type.delete()
        logger.info(f'Product type {pk} deleted')
        return redirect('product_types_list')

    return render(request, 'products/delete_product_type.html', {'product_type': product_type})

@login_required
def products_list(request):
    logger.info('Products list page accessed')
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {'products': products})

@login_required
def create_product(request):
    logger.info('Create product page accessed')
    if not request.user.is_superuser:
        return redirect('products_list')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            logger.info('Product created')
            return redirect('products_list')
    else:
        form = ProductForm()

    return render(request, 'products/create_product.html', {'form': form})

@login_required
def update_product(request, pk):
    logger.info(f'Update product page accessed for product {pk}')
    product = Product.objects.get(pk=pk)
    if not request.user.is_superuser:
        return redirect('products_list')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            logger.info(f'Product {pk} updated')
            return redirect('products_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/update_product.html', {'form': form, 'product': product})

@login_required
def delete_product(request, pk):
    logger.info(f'Delete product page accessed for product {pk}')
    product = Product.objects.get(pk=pk)
    if not request.user.is_superuser:
        return redirect('products_list')

    if request.method == 'POST':
        product.delete()
        logger.info(f'Product {pk} deleted')
        return redirect('products_list')

    return render(request, 'products/delete_product.html', {'product': product})

@login_required
def admin_dashboard(request):
    logger.info('Admin dashboard page accessed')
    if not request.user.is_superuser:
        logger.warning('Non-superuser attempted to access admin dashboard')
        return HttpResponseForbidden()
    
    price_list = Product.objects.all()
    logger.info('Retrieved product list')
    city_customers = get_city_customers()
    logger.info('Retrieved city customers')
    
    # Мебель, пользующаяся наибольшим спросом
    build_product_popularity()
    logger.info('Built product popularity ranking')
    
    # Ежемесячный объем продаж мебели каждого вида
    monthly_sales = Order.objects.values('product__name', 'date__month').annotate(total_quantity=Sum('quantity'))
    logger.info('Retrieved monthly sales data')
    
    # Годовой отчет поступлений от продаж
    annual_revenue = Order.objects.values('date__year').annotate(total_revenue=Sum('revenue'))
    logger.info('Retrieved annual revenue data')
    
    # Построение тренда
    monthly_sales = get_monthly_sales()
    logger.info('Retrieved monthly sales data for trend calculation')
    trends = calculate_linear_trend(monthly_sales)
    logger.info('Calculated linear trend')
    forecast = make_sales_forecast(trends, 4)  # forecast for next month
    logger.info('Made sales forecast for next month')
    plot_sales_data(monthly_sales, trends)
    logger.info('Plotted sales data')
    
    return render(request, 'products/admin_dashboard.html', {
        'products': price_list,
        'city_customers': city_customers,
        'annual_revenue': annual_revenue,
        'onthly_sales': monthly_sales,
        'onth_names': MONTH_NAMES,
    })
    logger.info('Rendered admin dashboard template')