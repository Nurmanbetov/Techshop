from django.test import TestCase, Client
from django.urls import reverse 
from .models import Product
from selenium import webdriver
from time import sleep



class ProductsTestCase(TestCase):
    def setUp(self):
        products_url = reverse("products")
        c = Client()
        self.response = c.get(products_url)
        self.products = Product.objects.all()

    def test_products_open_200_OK(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Все товары")
        self.assertContains(self.response, "Все продавцы")


class InitTestCase(TestCase):
    def test_load_init_page_success(self):
        driver =  webdriver.Chrome()
        driver.get("localhost:8000")
        sleep(3)
        driver.find_element_by_xpath("//a[contains(@href, '/product/all/')]").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(@href, '/sellers/')]").click()
        sleep(3)

        self.assertIn("form", driver.page_source)