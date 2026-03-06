from selenium import webdriver
from pages.base_page import BasePage
import allure

class TestNaviationButtons:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка перехода на главную странцу при клике по логотипу Самокат') 
    @allure.description('Переход с главной страницы на страницу заказа самоката, поиск и клик логотипа Самокат с проверкой текущей ссылки после перехода')
    def test_scooter_logo_redirect_to_main_page(self):
        base_page = BasePage(self.driver)
        base_page.open_base_page()
        base_page.click_base_order_button()
        assert base_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/order'
        base_page.click_logo_button()
        assert base_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/', 'Открытая страница не совпадает с главной'

    @allure.title('Проверка открытия нового окна с сайтом Дзен при нажатии на логотип Яндекса') 
    @allure.description('Поиск и клик логотипа Яндекса с переходом в новое окно и проверкой ссылки в новом окне')
    def test_yandex_logo_opens_dzen_in_new_tab(self):
        base_page = BasePage(self.driver)
        base_page.open_base_page()
        base_page.click_yandex_button()
        base_page.wait_for_new_window()
        base_page.switch_to_new_window()
        base_page.wait_dzen_loading()
        assert 'dzen.ru' in base_page.get_current_url(), 'Редирект на Dzen не происходит'
        base_page.switch_to_main_window()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    