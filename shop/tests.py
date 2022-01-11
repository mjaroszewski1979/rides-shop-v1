
# Django imports
from django.test import TestCase, Client
from django.urls import reverse, resolve


# App imports
from .models import Category, Car
from .views import index, about, expedition, racing, speed, vintage, car, cars, category


# Testing shop app
class ShopTest(TestCase):

    def setUp(self):
        self.client = Client()
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


    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_index_get(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Rides Shop |  Home', status_code=200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_post(self):
        data={
            'name' : 'maciej',
            'email' : 'mj@gmail.com',
            'message' : 'new message'
        }
        response = self.client.post(reverse('index'), data, follow=True)
        self.assertContains(response, 'Rides Shop |  Home', status_code=200)
        self.assertTrue(b'Thank you maciej for your message. We will reply to you as soon as possible at mj@gmail.com.' in response.content)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_about_get(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, 'Rides Shop |  About', status_code=200)
        self.assertTemplateUsed(response, 'about.html')

    def test_expedition_url_is_resolved(self):
        url = reverse('expedition')
        self.assertEquals(resolve(url).func, expedition)

    def test_expedition_get(self):
        response = self.client.get(reverse('expedition'))
        self.assertContains(response, 'Rides Shop |  Expedition', status_code=200)
        self.assertTemplateUsed(response, 'expedition.html')

    def test_racing_url_is_resolved(self):
        url = reverse('racing')
        self.assertEquals(resolve(url).func, racing)

    def test_racing_get(self):
        response = self.client.get(reverse('racing'))
        self.assertContains(response, 'Rides Shop |  Racing', status_code=200)
        self.assertTemplateUsed(response, 'racing.html')

    def test_speed_url_is_resolved(self):
        url = reverse('speed')
        self.assertEquals(resolve(url).func, speed)

    def test_speed_get(self):
        response = self.client.get(reverse('speed'))
        self.assertContains(response, 'Rides Shop |  Speed', status_code=200)
        self.assertTemplateUsed(response, 'speed.html')

    def test_vintage_url_is_resolved(self):
        url = reverse('vintage')
        self.assertEquals(resolve(url).func, vintage)

    def test_vintage_get(self):
        response = self.client.get(reverse('vintage'))
        self.assertContains(response, 'Rides Shop |  Vintage', status_code=200)
        self.assertTemplateUsed(response, 'vintage.html')

    def test_car_url_is_resolved(self):
        url = reverse('car', args= (self.new_car.slug, ))
        self.assertEquals(resolve(url).func, car)

    def test_car_get(self):
        response = self.client.get(reverse('car', args= (self.new_car.slug, )))
        self.assertContains(response, 'Rides Shop |  Car', status_code=200)
        self.assertTemplateUsed(response, 'car.html')
        self.assertIsNotNone(response.context['car'])

    def test_category_url_is_resolved(self):
        url = reverse('category', args= (self.new_category.slug, ))
        self.assertEquals(resolve(url).func, category)

    def test_category_get(self):
        response = self.client.get(reverse('category', args= (self.new_category.slug, )))
        self.assertContains(response, 'Rides Shop |  Category', status_code=200)
        self.assertTemplateUsed(response, 'category.html')
        self.assertIsNotNone(response.context['page_obj'])

    def test_cars_url_is_resolved(self):
        url = reverse('cars')
        self.assertEquals(resolve(url).func, cars)

    def test_cars_get(self):
        response = self.client.get(reverse('cars'))
        self.assertContains(response, 'Rides Shop |  Cars', status_code=200)
        self.assertTemplateUsed(response, 'cars.html')
        self.assertIsNotNone(response.context['page_obj'])

    def test_cars_post(self):
        data={
            'producer' : 'ferrari'
        }
        response = self.client.post(reverse('cars'), data, follow=True)
        self.assertContains(response, 'Rides Shop |  Cars', status_code=200)
        self.assertTrue(b'<a href="/car/ferrari/" class="image">' in response.content)

    def test_car_model(self):
        car_obj = Car(
        category = self.new_category,
        producer = 'audi',
        slug = 'audi',
        description = 'this is audi',
        country_of_origin = 'germany',
        colour = 'black',
        production_year = '2021',
        number_of_doors = '3',
        electric = True,
        first_owner = False,
        price = 70000
        )
        car_obj.save()
        cars = Car.objects.all()
        car_obj_print = str(Car.objects.get(producer=car_obj.producer))
        self.assertIsNotNone(car_obj)
        self.assertEquals(cars.count(), 2)
        self.assertEquals(car_obj.category, self.new_category)
        self.assertEquals(car_obj.producer, 'audi')
        self.assertEquals(car_obj.slug, 'audi')
        self.assertEquals(car_obj.description, 'this is audi')
        self.assertEquals(car_obj.country_of_origin, 'germany')
        self.assertEquals(car_obj.colour, 'black')
        self.assertEquals(car_obj.production_year, '2021')
        self.assertEquals(car_obj.number_of_doors, '3')
        self.assertEquals(car_obj.electric, True)
        self.assertEquals(car_obj.first_owner, False)
        self.assertEquals(car_obj.price, 70000)
        self.assertEquals(car_obj_print, str(car_obj.producer))

    def test_category_model(self):
        cat_obj = Category(
            title = 'vintage',
            slug = 'vintage'
        )
        cat_obj.save()
        categories = Category.objects.all()
        cat_obj_print = str(Category.objects.get(title=cat_obj.title))
        self.assertIsNotNone(cat_obj)
        self.assertEquals(categories.count(), 2)
        self.assertEquals(cat_obj.title, 'vintage')
        self.assertEquals(cat_obj.slug, 'vintage')
        self.assertEquals(cat_obj_print, str(cat_obj.title))
