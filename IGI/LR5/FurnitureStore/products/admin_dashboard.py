from django.db.models import Sum, Count
import matplotlib.pyplot as plt
from .models import Product, Customer, Order, Promocode, PickupPoint, ProductType
import numpy as np
import matplotlib
matplotlib.use('Agg')

import itertools


def get_city_customers():
    customers = Customer.objects.all()
    city_customers = {}
    for customer in customers:
        if customer.city not in city_customers:
            city_customers[customer.city] = []
        city_customers[customer.city].append(customer)
    
    return city_customers


def build_product_popularity():
    plt.clf()
    most_popular_products = Order.objects.values('product__name').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')[:2]
    least_popular_products = Order.objects.values('product__name').annotate(total_quantity=Sum('quantity')).order_by('total_quantity')[:2]

    popular_product_names = [product['product__name'] for product in most_popular_products]
    popular_product_quantities = [product['total_quantity'] for product in most_popular_products]

    least_popular_product_names = [product['product__name'] for product in least_popular_products]
    least_popular_product_quantities = [product['total_quantity'] for product in least_popular_products]

    plt.bar(popular_product_names, popular_product_quantities, label='Most Popular', color='green')  
    plt.bar(least_popular_product_names, least_popular_product_quantities, label='Least Popular', color='red')

    plt.xlabel('Название')
    plt.ylabel('Кол-во заказов')
    plt.title('Популярность товаров')

    plt.savefig('static/popular_products_chart.png')
    
    
def get_monthly_sales():
    return Order.objects.values('product__name', 'date__month').annotate(total_quantity=Sum('quantity'))

def calculate_linear_trend(monthly_sales):
    trends = {}
    for product in monthly_sales.values('product__name').distinct():
        product_name = product['product__name']
        product_data = monthly_sales.filter(product__name=product_name)
        
        months = [row['date__month'] for row in product_data]
        quantities = [row['total_quantity'] for row in product_data]
        
        coefficients = np.polyfit(months, quantities, 1)
        trend = np.poly1d(coefficients)
        
        trends[product_name] = trend
    return trends

def make_sales_forecast(trends, next_month):
    forecast = {}
    for product_name, trend in trends.items():
        forecast_quantity = trend(next_month)
        forecast[product_name] = forecast_quantity
    return forecast

def plot_sales_data(monthly_sales, trends):
    plt.clf()
    
    # Первая фигура и оси
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    
    for i, (product_name, trend) in enumerate(itertools.islice(trends.items(), 5)):
        product_data = monthly_sales.filter(product__name=product_name)
        
        months = [row['date__month'] for row in product_data]
        quantities = [row['total_quantity'] for row in product_data]
        
        ax1.plot(months, quantities, 'o-', label=product_name)
    
    ax1.set_title('Ежемесячные продажи')
    ax1.set_xlabel('Месяц')
    ax1.set_ylabel('Количество')
    
    ax1.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))  # Изменено на 'center left' и добавлен bbox_to_anchor
    
    # Вторая фигура и оси
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    
    for i, (product_name, trend) in enumerate(itertools.islice(trends.items(), 5)):
        x = np.arange(1, 12)  # months 1-12
        y = trend(x)
        ax2.plot(x, y, '--', label=f'{product_name}: линейный тренд')
    
    ax2.set_title('Линейный тренд')
    ax2.set_xlabel('Месяц')
    ax2.set_ylabel('Предполагаемое количество')
    
    ax2.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))  # Изменено на 'center left' и добавлен bbox_to_anchor
    
    # Сохранение графиков
    fig1.savefig('static/monthly_sales.png', bbox_inches='tight')
    fig2.savefig('static/linear_trends.png', bbox_inches='tight')