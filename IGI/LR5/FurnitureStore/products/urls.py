from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^products/create/$', views.create_product, name='create_product'),
    re_path(r'^products/(?P<pk>\d+)/update/$', views.update_product, name='update_product'),
    re_path(r'^products/(?P<pk>\d+)/delete/$', views.delete_product, name='delete_product'),
    re_path(r'^products/(?P<pk>\d+)/$', views.product_detail, name='product_detail'),
    re_path(r'^products/$', views.products_list, name='products_list'),

    re_path(r'^orders/create/(?P<product_id>\d+)$', views.create_order, name='create_order'),
    re_path(r'^search/$', views.search_products, name='search_products'),
    re_path(r'^filter/$', views.filter_products, name='filter_products'),
    re_path(r'^orders/$', views.user_orders, name='orders'),

    re_path(r'^employee_dashboard/$', views.employee_dashboard, name='employee_dashboard'),
    re_path(r'^create_product/$', views.create_product, name='create_product'),

    re_path(r'^promocodes/create/$', views.create_promocode, name='create_promocode'),
    re_path(r'^promo_codes/(?P<pk>\d+)/update/$', views.update_promocode, name='update_promocode'),
    re_path(r'^promo_codes/(?P<pk>\d+)/delete/$', views.delete_promocode, name='delete_promocode'),
    re_path(r'^promo_codes/$', views.promo_codes, name='promo_codes'),

    re_path(r'^pickup_points/create/$', views.create_pickup_point, name='create_pickup_point'),
    re_path(r'^pickup_points/(?P<pk>\d+)/update/$', views.update_pickup_point, name='update_pickup_point'),
    re_path(r'^pickup_points/(?P<pk>\d+)/delete/$', views.delete_pickup_point, name='delete_pickup_point'),
    re_path(r'^pickup_points/$', views.pickup_points_list, name='pickup_points_list'),

    re_path(r'^product_types/create/$', views.create_product_type, name='create_product_type'),
    re_path(r'^product_types/(?P<pk>\d+)/update/$', views.update_product_type, name='update_product_type'),
    re_path(r'^product_types/(?P<pk>\d+)/delete/$', views.delete_product_type, name='delete_product_type'),
    re_path(r'^product_types/$', views.product_types_list, name='product_types_list'),

    re_path(r'^price_list/$', views.price_list, name='price_list'),
    re_path(r'^customer_list/$', views.customer_list, name='customer_list'),

    re_path(r'^dashboard/$', views.admin_dashboard, name='admin_dashboard'),
]