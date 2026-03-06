from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
import pytest
import allure


class TestScooterOrder:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка заказа самоката с заполнением всех обязательных полей двумя наборами данных') 
    @allure.description('Поиск и заполненине все обязательных для заказа полей и проверка наличия статуса "Заказ оформлен"')
    @pytest.mark.parametrize("order_button,name,surname,address,metro,phone,date,duration", [
        ("main","Анатолий","Курьеров","Москва, Кремлёвская набережная, 1", "Лубянка", "12398765431", "12.05.2026", "сутки"),
        ("base","Лев","Самокатов", "Москва, Чистопрудный бульвар, 13", "Чистые пруды", "32145678902", "13.06.2026", "трое суток" )])
    def test_scooter_order_pozitive(self,order_button,name,surname,address,metro,phone,date,duration):
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)
        main_page.open_main_page()
        main_page.choose_order_button(order_button)
        order_page.wait_order_page_loading()
        order_page.order_scooter(name, surname, address, metro, phone, date, duration)
        assert 'Заказ оформлен' in order_page.get_order_status(), "Произошла ошибка при оформлении заказа"


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()     
