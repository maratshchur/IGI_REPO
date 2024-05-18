from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product, ProductType, PickupPoint, Order, Promocode
from users.models import Customer, User

class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()
        self.product_type = ProductType.objects.create(name='Test Product Type')
        self.product = Product.objects.create(name='Test Product', code=1, product_type=self.product_type, model='Test Model', price=10.99, production_time=1, image='test_image.jpg')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/home.html')
        self.assertContains(response, self.product.name)

class TestProductDetailView(TestCase):
    def setUp(self):
        self.client = Client()
        self.product_type = ProductType.objects.create(name='Test Product Type')
        self.product = Product.objects.create(name='Test Product', code=1, product_type=self.product_type, model='Test Model', price=10.99, production_time=1, image='test_image.jpg')

    def test_product_detail_view(self):
        response = self.client.get(reverse('product_detail', args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertContains(response, self.product.name)

class TestSearchProductsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.product_type = ProductType.objects.create(name='Test Product Type')
        self.product = Product.objects.create(name='Test Product', code=1, product_type=self.product_type, model='Test Model', price=10.99, production_time=1, image='test_image.jpg')

    def test_search_products_view(self):
        response = self.client.get(reverse('search_products'), {'q': 'Test Product'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/home.html')
        self.assertContains(response, self.product.name)

class TestFilterProductsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.product_type = ProductType.objects.create(name='Test Product Type')
        self.product = Product.objects.create(name='Test Product', code=1, product_type=self.product_type, model='Test Model', price=10.99, production_time=1, image='test_image.jpg')

    def test_filter_products_view(self):
        response = self.client.get(reverse('filter_products'), {'price_min': 10, 'price_max': 20, 'product_type': self.product_type.name})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/home.html')
        self.assertContains(response, self.product.name)

class TestCreateOrderView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.customer = Customer.objects.create(user=self.user, city='Test City', address='Test Address', phone='1234567890')
        self.product_type = ProductType.objects.create(name='Test Product Type')
        self.product = Product.objects.create(name='Test Product', code=1, model='Test Model', price=10.99, production_time=1, image='test_image.jpg', product_type=self.product_type)
        self.client.login(username='testuser', password='testpassword')

    def test_create_order_view(self):
        response = self.client.get(reverse('create_order', args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/create_order.html')


class TestPromoCodesView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.customer = Customer.objects.create(user=self.user, city='Test City', address='Test Address', phone='1234567890')
        self.promocode = Promocode.objects.create(name='Test Promocode', description='Test description', code='TESTCODE', discount=10.00)
        self.client.login(username='testuser', password='testpassword')

    def test_promo_codes_view(self):
        response = self.client.get(reverse('promo_codes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/promo_codes.html')


class TestCreateProductView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword', is_superuser=True)
        self.client.login(username='testuser', password='testpassword')

    def test_create_product_view(self):
        response = self.client.get(reverse('create_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/create_product.html')

class TestPickupPointsListView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.customer = Customer.objects.create(user=self.user, city='Test City', address='Test Address', phone='1234567890')
        self.pickup_point = PickupPoint.objects.create(name='Test Pickup Point', address='Test Address')
        self.client.login(username='testuser', password='testpassword')

    def test_pickup_points_list_view(self):
        response = self.client.get(reverse('pickup_points_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/pickup_points_list.html')
        self.assertContains(response, self.pickup_point.name)

class TestCreatePickupPointView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword', is_superuser=True)
        self.client.login(username='testuser', password='testpassword')

    def test_create_pickup_point_view(self):
        response = self.client.get(reverse('create_pickup_point'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/create_pickup_point.html')

    def test_create_pickup_point_view_post(self):
        response = self.client.post(reverse('create_pickup_point'), {'name': 'Test Pickup Point', 'address': 'Test Address'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('pickup_points_list'))

class TestUpdatePickupPointView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword', is_superuser=True)
        self.pickup_point = PickupPoint.objects.create(name='Test Pickup Point', address='Test Address')
        self.client.login(username='testuser', password='testpassword')

    def test_update_pickup_point_view(self):
        response = self.client.get(reverse('update_pickup_point', args=[self.pickup_point.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/update_pickup_point.html')

    def test_update_pickup_point_view_post(self):
        response = self.client.post(reverse('update_pickup_point', args=[self.pickup_point.pk]), {'name': 'Updated Test Pickup Point', 'address': 'Updated Test Address'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('pickup_points_list'))

class TestDeletePickupPointView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword', is_superuser=True)
        self.pickup_point = PickupPoint.objects.create(name='Test Pickup Point', address='Test Address')
        self.client.login(username='testuser', password='testpassword')

    def test_delete_pickup_point_view(self):
        response = self.client.get(reverse('delete_pickup_point', args=[self.pickup_point.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/delete_pickup_point.html')

    def test_delete_pickup_point_view_post(self):
        response = self.client.post(reverse('delete_pickup_point', args=[self.pickup_point.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('pickup_points_list'))


class TestProductsViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')
        self.client.login(username='testuser', password='password')
        self.product_type = ProductType.objects.create(name='Test Product Type')
        self.product = Product.objects.create(name='Test Product', code=1, model='Test Model', price=10.99, production_time=1, image='test_image.jpg', product_type=self.product_type)

    def test_products_list_view(self):
        response = self.client.get(reverse('products_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products_list.html')
        self.assertContains(response, self.product.name)

    def test_create_product_view_get(self):
        response = self.client.get(reverse('create_product'))
        self.assertEqual(response.status_code, 302)

    def test_create_product_view_post(self):
        data = {
            'name': 'New Test Product',
            'code': 2,
            'odel': 'New Test Model',
            'price': 20.99,
            'production_time': 2,
            'image': 'new_test_image.jpg',
            'product_type': self.product_type.pk
        }
        response = self.client.post(reverse('create_product'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products_list'))

    def test_update_product_view_get(self):
        response = self.client.get(reverse('update_product', args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)

    def test_update_product_view_post(self):
        data = {
            'name': 'Updated Test Product',
            'code': 3,
            'odel': 'Updated Test Model',
            'price': 30.99,
            'production_time': 3,
            'image': 'updated_test_image.jpg',
            'product_type': self.product_type.pk
        }
        response = self.client.post(reverse('update_product', args=[self.product.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products_list'))

    def test_delete_product_view_get(self):
        response = self.client.get(reverse('delete_product', args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)

    def test_delete_product_view_post(self):
        response = self.client.post(reverse('delete_product', args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products_list'))

    def test_non_superuser_access(self):
        self.user.is_superuser = False
        self.user.save()
        response = self.client.get(reverse('create_product'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products_list'))
        response = self.client.get(reverse('update_product', args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products_list'))
        response = self.client.get(reverse('delete_product', args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products_list'))