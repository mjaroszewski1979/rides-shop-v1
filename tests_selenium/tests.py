from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from . import page
from shop.models import Car, Category
from django.urls import reverse


class UrbanTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome('tests_selenium/chromedriver.exe')
        
        self.driver.set_window_size(1920, 1080)
        self.new_category = Category.objects.create(title='speed', slug='speed')
        self.new_category.save()
        self.new_car = Car(
        category = self.new_category,
        producer = 'ferrari',
        slug = 'ferrari',
        description = 'this is ferrari',
        country_of_origin = 'italy',
        colour = 'white',
        production_year = '2020',
        number_of_doors = '3',
        electric = True,
        first_owner = False,
        price = 50000
        )
        self.new_car.save()


    def tearDown(self):
        self.driver.close()


    def test_indexpage(self):
        self.driver.get(self.live_server_url)
        index_page = page.IndexPage(self.driver)
        assert index_page.is_title_matches()
        assert index_page.is_index_heading_displayed_correctly()
        assert index_page.is_about_link_works()
        assert index_page.is_index_link_works()
        assert index_page.is_contact_form_works()
        assert index_page.is_speed_link_works()

    def test_speed_page(self):
        self.driver.get(self.live_server_url + reverse('speed'))
        speed_page = page.SpeedPage(self.driver)
        assert speed_page.is_title_matches()
        assert speed_page.is_offers_link_works()
        assert speed_page.is_car_producer_displayed_coorectly()

    def test_cars_page(self):
        self.driver.get(self.live_server_url + reverse('cars'))
        cars_page = page.CarsPage(self.driver)
        assert cars_page.is_title_matches()
        assert cars_page.is_cars_heading_displayed_correctly()
        assert cars_page.is_filter_form_works()
        assert cars_page.is_detail_link_works()
        assert cars_page.is_menu_button_works()
        assert cars_page.is_home_link_works()
        assert cars_page.is_category_link_works()




        