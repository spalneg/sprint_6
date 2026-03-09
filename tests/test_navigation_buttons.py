from selenium import webdriver
from pages.main_page import MainPage
import allure
from urls import *

class TestNaviationButtons:

    @allure.title('Проверка перехода на главную странцу при клике по логотипу Самокат') 
    @allure.description('Переход с главной страницы на страницу заказа самоката, поиск и клик логотипа Самокат с проверкой текущей ссылки после перехода')
    def test_scooter_logo_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_base_order_button()
        assert main_page.get_current_url() == ORDER_URL
        main_page.click_logo_button()
        assert main_page.get_current_url() == BASE_URL, 'Открытая страница не совпадает с главной'

    @allure.title('Проверка открытия нового окна с сайтом Дзен при нажатии на логотип Яндекса') 
    @allure.description('Поиск и клик логотипа Яндекса с переходом в новое окно и проверкой ссылки в новом окне')
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_yandex_button()
        main_page.wait_for_new_window()
        main_page.switch_to_new_window()
        main_page.wait_dzen_loading()
        assert 'dzen.ru' in main_page.get_current_url(), 'Редирект на Dzen не происходит'
        main_page.switch_to_main_window()


    