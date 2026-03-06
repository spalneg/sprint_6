from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators as bp
import allure


class BasePage:
    
    def __init__(self, driver):

        self.driver = driver
    
    @allure.step('Открыть главную страницу')       
    def open_base_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

    @allure.step('Клик по кнопке "заказать" на главной странице')
    def click_base_order_button(self):
        self.driver.find_element(*bp.base_order_button).click()
    
    @allure.step('Клик по логотипу Самокат')
    def click_logo_button(self):
        self.driver.find_element(*bp.logo_button).click()

    @allure.step('Клик по логотипу Яндекс')
    def click_yandex_button(self):
        self.driver.find_element(*bp.yandex_button).click()
    
    @allure.step('Ожидание открытия нового окна')
    def wait_for_new_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))

    @allure.step('Получение URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Переключение на новое окно')
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание открытия сайта Дзен')
    def wait_dzen_loading(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(bp.dzen_locator)) 

    @allure.step('Переключение на основное окно')
    def switch_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

