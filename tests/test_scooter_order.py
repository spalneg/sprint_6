from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import order_data
import pytest
import allure


class TestScooterOrder:

    @allure.title('Проверка заказа самоката с заполнением всех обязательных полей двумя наборами данных') 
    @allure.description('Поиск и заполненине все обязательных для заказа полей и проверка наличия статуса "Заказ оформлен"')
    @pytest.mark.parametrize("order_button,name,surname,address,metro,phone,date,duration", order_data)
    def test_scooter_order_pozitive(self, driver, order_button, name, surname, address, metro, phone, date, duration):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_main_page()
        main_page.choose_order_button(order_button)
        main_page.close_cookie()
        order_page.wait_order_page_loading()
        order_page.order_scooter(name, surname, address, metro, phone, date, duration)
        assert 'Заказ оформлен' in order_page.get_order_status(), "Произошла ошибка при оформлении заказа"
