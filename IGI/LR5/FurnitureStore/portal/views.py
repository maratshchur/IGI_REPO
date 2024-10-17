from django.shortcuts import get_object_or_404, render, redirect
import requests
from .forms import ReviewForm
from .models import Article, CompanyInfo, News, Term,  Vacancy, Review
from django.contrib.auth.decorators import login_required

import logging

logger = logging.getLogger('db_logger')


def index(request):
    logger.info('Index page viewed')
    latest_article = Article.objects.latest('created_at')
    return render(request, 'portal/index.html', {'latest_article': latest_article})

def about(request):
    logger.info('About page viewed')
    company_info = CompanyInfo.objects.first()
    return render(request, 'portal/about.html', {'company_info': company_info})

def news(request):
    logger.info('News page viewed')
    news_list = News.objects.all()
    return render(request, 'portal/news.html', {'news_list': news_list})

def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    return render(request, 'portal/news_detail.html', {'news': news})

def dictionary(request):
    logger.info('Dictionary page viewed')
    terms = Term.objects.all()
    return render(request, 'portal/dictionary.html', {'terms': terms})

def privacy_policy(request):
    logger.info('Privacy policy page viewed')
    return render(request, 'portal/privacy_policy.html')

def vacancies(request):
    logger.info('Vacancies page viewed')
    vacancies_list = Vacancy.objects.all()
    return render(request, 'portal/vacancies.html', {'vacancies_list': vacancies_list})

def reviews(request):
    logger.info('Reviews page viewed')
    reviews_list = Review.objects.all()
    return render(request, 'portal/reviews.html', {'reviews_list': reviews_list})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user.customer
            review.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    
    return render(request, 'portal/add_review.html', {'form': form})

@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user.user == request.user:
        review.delete()
    return redirect('reviews')

@login_required
def quote_of_the_day(request):
    logger.info('Quote of the day page viewed')
    response = requests.get('https://favqs.com/api/qotd')
    data = response.json()
    quote = data['quote']
    return render(request, 'portal/quote_of_the_day.html', {'quote': quote})

@login_required
def person_of_the_day(request):
    logger.info('Person of the day page viewed')
    name = request.GET.get('name')
    if name:
        response = requests.get(f'https://api.genderize.io/?name={name}')
        data = response.json()
        if data['gender'] is not None:
            gender = data['gender']
            probability = data['probability']
            logger.info(f'Gender detected for {name}: {gender} with probability {probability*100}%')
            return render(request, 'portal/person_gender.html', {'name': name, 'gender': gender, 'probability': probability*100})
        else:
            logger.info(f'Failed to detect gender for {name}')
            return render(request, 'portal/person_gender.html', {'name': name, 'gender': 'Не удалось определить пол', 'probability': ''})
    else:
        logger.info('No name provided')
        return render(request, 'portal/person_gender.html', {'name': '', 'gender': '', 'probability': ''})

def html_tags(request):
    return render(request, 'portal/html_learning.html')