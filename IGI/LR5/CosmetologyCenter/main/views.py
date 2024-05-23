from django.shortcuts import render, redirect
from services.models import Service, ServiceType
from .models import News, FAQ, Review, Banner, Promotional_code, Job
from .form import ReviewForm
import requests
import logging
from django.test import TestCase, Client
from django.urls import reverse
from .models import News, FAQ, Review, Banner, Promotional_code, Job
from services.models import Service, ServiceType


logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    logger.info('Method home')

    services = Service.objects.all()[:2]
    news = News.objects.first()
    banners = Banner.objects.all()

    return render(request, 'main/home.html', context={'services': services, 'news': news, 'banners': banners})

def about(request):
    return render(request, 'main/about.html')

def price_list(request):
    logger.info('Method price_list')

    service_types = ServiceType.objects.all()
    services_by_type = {}
    
    for service_type in service_types:
        services = Service.objects.filter(service_type=service_type)
        services_by_type[service_type] = services

    return render(request, 'main/price-list.html', {'services_by_type': services_by_type, 'service_types': service_types})


def news(request):
    logger.info('Method news')
    
    news = News.objects.all()
    return render(request, 'main/news.html', {'news': news})


def faq(request):
    logger.info('Method faq')

    faq = FAQ.objects.all()
    return render(request, 'main/FAQ.html', {'faq': faq})


def privacy_policy(request):
    logger.info('Method privacy_policy')

    return render(request, 'main/privacy_policy.html')



def reviews(request):
    logger.info('Method reviews')

    reviews = Review.objects.all()
    return render(request, 'main/reviews.html', {'reviews': reviews})


def create_review(request):
    logger.info('Method create_review')

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review.objects.create(text=request.POST.get('text'),
                                           rating=request.POST.get('rating'),
                                           author=request.POST.get('author'),
                                           ),

            return redirect('main:rewiews')

    else:
        form = ReviewForm()
        return render(request, "main/create_review.html", {"form": form})
    return redirect('main:home')


def sandbox(request):
    logger.info('Method sandbox')

    joke = requests.get('https://official-joke-api.appspot.com/jokes/random').json()
    dog = requests.get('https://dog.ceo/api/breeds/image/random').json()

    return render(request, 'main/sandbox.html',context={'joke': joke['setup'] + joke['punchline'], 
                                                  'dog': dog['message']})


def promotional_code(request):
    actual_promotional_code = Promotional_code.objects.filter(is_actual=True)
    archive_promotional_code = Promotional_code.objects.filter(is_actual=False)
    return render(request, 'main/promotional_code.html', {'actual_promotional_code': actual_promotional_code, 'archive_promotional_code': archive_promotional_code})


def vacancies(request):
    vacancies = Job.objects.filter(is_actual=True)
    return render(request, 'main/job.html', {'vacancies': vacancies})


def my_view(request):
    logger.debug('Это сообщение с уровнем DEBUG')
    logger.info('Это сообщение с уровнем INFO')
    logger.warning('Это сообщение с уровнем WARNING')
    logger.error('Это сообщение с уровнем ERROR')
    logger.critical('Это сообщение с уровнем CRITICAL')

class MainViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.service_type = ServiceType.objects.create(name='Test Service Type')
        self.service = Service.objects.create(name='Test Service', price=100, service_type=self.service_type)
        self.news = News.objects.create(title='Test News', content='Test Content')
        self.banners = Banner.objects.create(title='Test Banner', image='test_image.jpg')
        self.faq = FAQ.objects.create(question='Test Question', answer='Test Answer')
        self.review = Review.objects.create(text='Test Review', rating=5, author='Test Author')
        self.promotional_code = Promotional_code.objects.create(code='Test Code', is_actual=True)
        self.job = Job.objects.create(title='Test Job', description='Test Description', is_actual=True)

    def test_home_view(self):
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    def test_about_view(self):
        response = self.client.get(reverse('main:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about.html')

    def test_price_list_view(self):
        response = self.client.get(reverse('main:price_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/price-list.html')

    def test_news_view(self):
        response = self.client.get(reverse('main:news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/news.html')

    def test_faq_view(self):
        response = self.client.get(reverse('main:faq'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/FAQ.html')

    def test_privacy_policy_view(self):
        response = self.client.get(reverse('main:privacy_policy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/privacy_policy.html')

    def test_reviews_view(self):
        response = self.client.get(reverse('main:reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/reviews.html')

    def test_create_review_view(self):
        response = self.client.get(reverse('main:create_review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/create_review.html')

    def test_sandbox_view(self):
        response = self.client.get(reverse('main:sandbox'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/sandbox.html')

    def test_promotional_code_view(self):
        response = self.client.get(reverse('main:promotional_code'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/promotional_code.html')

    def test_vacancies_view(self):
        response = self.client.get(reverse('main:vacancies'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/job.html')

    def test_my_view(self):
        response = self.client.get(reverse('main:my_view'))
        self.assertEqual(response.status_code, 200)