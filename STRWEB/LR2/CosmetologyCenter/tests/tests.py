from datetime import date, timedelta
from django.test import TestCase, RequestFactory
from django.urls import reverse
from appointments.forms import AppointmentItemForm
from appointments.models import Appointment
from cart.context_processors import cart
from cart.models import Cart
from main.models import Client
from services.models import Service
from stats.views import calculate_age
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from stats.views import report
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from services.views import index, ServiceDetailView
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from main import views
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from doctors import views
from django.contrib.auth import views as auth_views
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from cart import views
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from appointments import views
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.utils import timezone
from main.models import Client
from appointments.models import Appointment
from datetime import datetime
from statistics import mean, median
from stats.views import report, calculate_age
import pandas as pd
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from services.models import Service
from services.views import index, ServiceDetailView
from django.test import TestCase, RequestFactory
from django.urls import reverse
from main.views import home, about, price_list, news, faq, sandbox, create_review, reviews, privacy_policy, promotional_code, vacancies
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from doctors.models import Doctor
from doctors.views import index, DoctorDetailView
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import home, sandbox
from cart.views import cart_details, add_to_cart, cart_remove
from doctors.views import index as doctors_index, DoctorDetailView
from services.views import index as services_index, ServiceDetailView
from appointments.views import appointment_list_for_user, create_appointment_item, create_appointments
from stats.views import report

from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from services.models import Service
from cart.views import add_to_cart, cart_details, cart_remove
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from appointments.views import appointment_list_for_user, create_appointment_item, create_appointments
from appointments.forms import AppointmentItemForm, ClientForm
from appointments.models import Appointment
from cart.models import Cart
from django.test import SimpleTestCase
from CosmetologyCenter.wsgi import application
from django.test import SimpleTestCase
from CosmetologyCenter.asgi import application
from django.test import TestCase, RequestFactory
from django.urls import reverse
from main.views import home, about, price_list, news, faq, sandbox, create_review, reviews, privacy_policy, promotional_code, vacancies
from django.test import TestCase
from django.test import RequestFactory

class MainViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_view(self):
        request = self.factory.get('/')
        response = home(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    def test_about_view(self):
        request = self.factory.get('/about/')
        response = about(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about.html')

    def test_price_list_view(self):
        request = self.factory.get('/prices/')
        response = price_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/price_list.html')

    def test_news_view(self):
        request = self.factory.get('/news/')
        response = news(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/news.html')

    def test_faq_view(self):
        request = self.factory.get('/FAQ/')
        response = faq(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/faq.html')

class AsgiTests(SimpleTestCase):

    def test_application_exists(self):
        self.assertIsNotNone(application)

class WsgiTests(SimpleTestCase):

    def test_application_exists(self):
        self.assertIsNotNone(application)

class AppointmentsViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_appointment_list_for_user_view(self):
        request = self.factory.get('/appointments/')
        request.user = self.user
        response = appointment_list_for_user(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointments/appointment-list.html')

    def test_create_appointment_item_view_get(self):
        request = self.factory.get('/appointments/create_appointment_item/')
        request.user = self.user
        response = create_appointment_item(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointments/create-appointment-item.html')
        self.assertIsInstance(response.context['form'], AppointmentItemForm)

    def test_create_appointment_item_view_post(self):
        request = self.factory.post('/appointments/create_appointment_item/', data={})
        request.user = self.user
        response = create_appointment_item(request)
        self.assertEqual(response.status_code, 200)  # Assuming form is invalid and it returns same page
        self.assertIsInstance(response.context['form'], AppointmentItemForm)

    def test_create_appointments_view_get(self):
        request = self.factory.get('/appointments/create_appointments/')
        response = create_appointments(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointments/create-client.html')
        self.assertIsInstance(response.context['form'], ClientForm)

    def test_create_appointments_view_post(self):
        request = self.factory.post('/appointments/create_appointments/', data={})
        response = create_appointments(request)
        self.assertEqual(response.status_code, 200)  # Assuming form is invalid and it returns same page
        self.assertIsInstance(response.context['form'], ClientForm)

class CartViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.service = Service.objects.create(name='Test Service', description='Test description', price=50)

    def test_add_to_cart_view(self):
        request = self.factory.post('/cart/add_to_cart/1/')
        request.user = self.user
        response = add_to_cart(request, service_id=1)
        self.assertEqual(response.status_code, 302)  # Should redirect to services-list
        self.assertEqual(len(request.session['cart']), 1)  # Check if item is added to the cart

    def test_cart_details_view(self):
        request = self.factory.get('/cart/')
        request.user = self.user
        response = cart_details(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart-detail.html')

    def test_cart_remove_view(self):
        # Add item to the cart
        request_add = self.factory.post('/cart/add_to_cart/1/')
        request_add.user = self.user
        add_to_cart(request_add, service_id=1)

        # Check if item is in the cart
        self.assertEqual(len(request_add.session['cart']), 1)

        # Remove item from the cart
        request_remove = self.factory.get('/cart/remove_in_cart/1/')
        request_remove.user = self.user
        response = cart_remove(request_remove, appointment_item_id=1)
        self.assertEqual(response.status_code, 302)  # Should redirect to cart_details
        self.assertEqual(len(request_remove.session['cart']), 0)  # Check if item is removed from the cart

class TestUrls(SimpleTestCase):

    def test_main_urls(self):
        url = reverse('main:home')
        self.assertEqual(resolve(url).func, home)

        url = reverse('main:sandbox')
        self.assertEqual(resolve(url).func, sandbox)

    def test_cart_urls(self):
        url = reverse('cart:cart_details')
        self.assertEqual(resolve(url).func, cart_details)

        url = reverse('cart:add_to_cart', args=[1])
        self.assertEqual(resolve(url).func, add_to_cart)

        url = reverse('cart:cart_remove', args=[1])
        self.assertEqual(resolve(url).func, cart_remove)

    def test_doctors_urls(self):
        url = reverse('doctors:doctors-list')
        self.assertEqual(resolve(url).func, doctors_index)

        url = reverse('doctors:doctor-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, DoctorDetailView)

    def test_services_urls(self):
        url = reverse('services:services-list')
        self.assertEqual(resolve(url).func, services_index)

        url = reverse('services:service-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, ServiceDetailView)

    def test_appointments_urls(self):
        url = reverse('appointments:appointment_list_for_user')
        self.assertEqual(resolve(url).func, appointment_list_for_user)

        url = reverse('appointments:create_appointment_item')
        self.assertEqual(resolve(url).func, create_appointment_item)

        url = reverse('appointments:create_appointments')
        self.assertEqual(resolve(url).func, create_appointments)

    def test_stats_urls(self):
        url = reverse('stats:report')
        self.assertEqual(resolve(url).func, report)

class DoctorsViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.doctor = Doctor.objects.create(name='Test Doctor', specialty='Test Specialty', bio='Test Bio')

    def test_index_view(self):
        request = self.factory.get('/doctors/')
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/doctors-list.html')

    def test_doctor_detail_view(self):
        url = reverse('doctors:doctor-detail', kwargs={'pk': self.doctor.pk})
        request = self.factory.get(url)
        request.user = self.user
        response = DoctorDetailView.as_view()(request, pk=self.doctor.pk)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/doctor-detail.html')
        self.assertEqual(response.context_data['doctor'], self.doctor)

class ServicesViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.service = Service.objects.create(name='Test Service', description='Test description', price=50)

    def test_index_view(self):
        request = self.factory.get('/services/')
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'services')

    def test_service_detail_view(self):
        url = reverse('services:service-detail', kwargs={'pk': self.service.pk})
        request = self.factory.get(url)
        request.user = self.user
        response = ServiceDetailView.as_view()(request, pk=self.service.pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'service')
        self.assertContains(response, 'form')
        self.assertIsInstance(response.context_data['form'], AppointmentItemForm)


class StatsViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

        # Создаем несколько клиентов и назначений для тестов
        self.client1 = Client.objects.create(first_name='John', last_name='Doe', date_of_birth=datetime(1990, 5, 15))
        self.client2 = Client.objects.create(first_name='Jane', last_name='Smith', date_of_birth=datetime(1985, 10, 20))
        self.appointment1 = Appointment.objects.create(client=self.client1, appointment_date=timezone.now())
        self.appointment2 = Appointment.objects.create(client=self.client2, appointment_date=timezone.now())

    def test_report_view(self):
        request = self.factory.get('/stats/report/')
        request.user = self.user
        response = report(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'average_age')
        self.assertContains(response, 'median_age')
        self.assertContains(response, 'image_base64_hist')

    def test_calculate_age(self):
        date_of_birth = datetime(1990, 5, 15)
        self.assertEqual(calculate_age(date_of_birth), 31)  # Assuming today is May 15, 2021

    def test_report_context(self):
        request = self.factory.get('/stats/report/')
        request.user = self.user
        response = report(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('average_age' in response.context)
        self.assertTrue('median_age' in response.context)
        self.assertTrue('image_base64_hist' in response.context)

    def test_dataframe_creation(self):
        # Создаем тестовые данные для проверки создания DataFrame
        prices = [50, 60, 70, 80, 90]
        appointments = [datetime.now(), datetime.now(), datetime.now(), datetime.now(), datetime.now()]
        df = pd.DataFrame({'sale_amount': prices, 'appointment_date': appointments})
        self.assertIsInstance(df, pd.DataFrame)

        # Проверяем, что DataFrame содержит ожидаемые столбцы
        self.assertTrue('sale_amount' in df.columns)
        self.assertTrue('appointment_date' in df.columns)


class TestAppointmentsUrls(SimpleTestCase):

    def test_appointment_list_for_user_url_is_resolved(self):
        url = reverse('appointments:appointment_list_for_user')
        self.assertEqual(resolve(url).func, views.appointment_list_for_user)

    def test_create_appointment_item_url_is_resolved(self):
        url = reverse('appointments:create_appointment_item')
        self.assertEqual(resolve(url).func, views.create_appointment_item)

    def test_create_appointments_url_is_resolved(self):
        url = reverse('appointments:create_appointments')
        self.assertEqual(resolve(url).func, views.create_appointments)


class TestCartUrls(SimpleTestCase):

    def test_cart_details_url_is_resolved(self):
        url = reverse('cart:cart_details')
        self.assertEqual(resolve(url).func, views.cart_details)

    def test_add_to_cart_url_is_resolved(self):
        url = reverse('cart:add_to_cart', args=[1])
        self.assertEqual(resolve(url).func, views.add_to_cart)

    def test_cart_remove_url_is_resolved(self):
        url = reverse('cart:cart_remove', args=[1])
        self.assertEqual(resolve(url).func, views.cart_remove)

class TestDoctorsUrls(SimpleTestCase):

    def test_doctors_list_url_is_resolved(self):
        url = reverse('doctors:doctors-list')
        self.assertEqual(resolve(url).func, views.index)

    def test_doctor_detail_url_is_resolved(self):
        url = reverse('doctors:doctor-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.DoctorDetailView)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)

    def test_password_change_url_is_resolved(self):
        url = reverse('password_change')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordChangeView)

    def test_password_change_done_url_is_resolved(self):
        url = reverse('password_change_done')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordChangeDoneView)

    def test_password_reset_url_is_resolved(self):
        url = reverse('password_reset')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetView)

    def test_password_reset_done_url_is_resolved(self):
        url = reverse('password_reset_done')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetDoneView)

    def test_password_reset_confirm_url_is_resolved(self):
        url = reverse('password_reset_confirm', args=['uidb64', 'token'])
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetConfirmView)

    def test_password_reset_complete_url_is_resolved(self):
        url = reverse('password_reset_complete')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetCompleteView)

class TestMainUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('main:home')
        self.assertEqual(resolve(url).func, views.home)

    def test_about_url_is_resolved(self):
        url = reverse('main:about')
        self.assertEqual(resolve(url).func, views.about)

    def test_price_list_url_is_resolved(self):
        url = reverse('main:price-list')
        self.assertEqual(resolve(url).func, views.price_list)

    def test_news_url_is_resolved(self):
        url = reverse('main:news')
        self.assertEqual(resolve(url).func, views.news)

    def test_faq_url_is_resolved(self):
        url = reverse('main:FAQ')
        self.assertEqual(resolve(url).func, views.faq)

    def test_sandbox_url_is_resolved(self):
        url = reverse('main:sandbox')
        self.assertEqual(resolve(url).func, views.sandbox)

    def test_create_review_url_is_resolved(self):
        url = reverse('main:create_rewiew')
        self.assertEqual(resolve(url).func, views.create_review)

    def test_reviews_url_is_resolved(self):
        url = reverse('main:rewiews')
        self.assertEqual(resolve(url).func, views.reviews)

    def test_privacy_policy_url_is_resolved(self):
        url = reverse('main:privacy_policy')
        self.assertEqual(resolve(url).func, views.privacy_policy)

    def test_promotional_code_url_is_resolved(self):
        url = reverse('main:promotional_code')
        self.assertEqual(resolve(url).func, views.promotional_code)

    def test_vacancies_url_is_resolved(self):
        url = reverse('main:vacancies')
        self.assertEqual(resolve(url).func, views.vacancies)
class TestServicesUrls(SimpleTestCase):

    def test_services_list_url_is_resolved(self):
        url = reverse('services:services-list')
        self.assertEqual(resolve(url).func, index)

    def test_service_detail_url_is_resolved(self):
        url = reverse('services:service-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, ServiceDetailView)
class TestStatsUrls(SimpleTestCase):

    def test_report_url_is_resolved(self):
        url = reverse('stats:report')
        self.assertEqual(resolve(url).func, report)

class ReportViewTestCase(TestCase):
    def test_calculate_age(self):
        age = calculate_age(date.today() - timedelta(days=365*30))
        self.assertEqual(age, 29)
