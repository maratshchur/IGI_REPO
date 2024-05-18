from django.urls import re_path
from. import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^news/$', views.news, name='news'),
    re_path(r'^dictionary/$', views.dictionary, name='dictionary'),
    re_path(r'^privacy_policy/$', views.privacy_policy, name='privacy_policy'),
    re_path(r'^vacancies/$', views.vacancies, name='vacancies'),
    re_path(r'^reviews/$', views.reviews, name='reviews'),
    re_path(r'^quote_of_the_day/$', views.quote_of_the_day, name='quote_of_the_day'),
    re_path(r'^person_gender/$', views.person_of_the_day, name='person_gender'),
]