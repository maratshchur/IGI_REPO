from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
from.models import Article, CompanyInfo, News, Term, Vacancy, Review
from.views import index, about, news, dictionary, privacy_policy, vacancies, reviews, quote_of_the_day, person_of_the_day
from users.models import User, Customer

class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.article = Article.objects.create(title="Test Article", content="Test content", image="test_image.jpg")
        self.company_info = CompanyInfo.objects.create(text="Test company info", logo="test_logo.jpg")
        self.news = News.objects.create(title="Test News", content="Test news content", image="test_news_image.jpg")
        self.term = Term.objects.create(question="Test question", answer="Test answer")
        self.vacancy = Vacancy.objects.create(title="Test Vacancy", description="Test vacancy description")
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.customer = Customer.objects.create(user=self.user, city="Test city", address="Test address", phone="Test phone")
        self.review = Review.objects.create(user=self.customer, rating=5, text="Test review")

    def test_index_view(self):
        request = self.factory.get(reverse('index'))
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.article.title)

    def test_news_view(self):
        request = self.factory.get(reverse('news'))
        response = news(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.news.title)

    def test_dictionary_view(self):
        request = self.factory.get(reverse('dictionary'))
        response = dictionary(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.term.question)

    def test_privacy_policy_view(self):
        request = self.factory.get(reverse('privacy_policy'))
        response = privacy_policy(request)
        self.assertEqual(response.status_code, 200)

    def test_vacancies_view(self):
        request = self.factory.get(reverse('vacancies'))
        response = vacancies(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.vacancy.title)

    def test_reviews_view(self):
        request = self.factory.get(reverse('reviews'))
        response = reviews(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.review.text)

    def test_quote_of_the_day_view(self):
        request = self.factory.get(reverse('quote_of_the_day'))
        request.user = self.user
        response = quote_of_the_day(request)
        self.assertEqual(response.status_code, 200)

    def test_person_of_the_day_view(self):
        request = self.factory.get(reverse('person_gender'))
        request.user = self.user
        response = person_of_the_day(request)
        self.assertEqual(response.status_code, 200)

        request.GET = {'name': 'John'}
        response = person_of_the_day(request)
        self.assertEqual(response.status_code, 200)