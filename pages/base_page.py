from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators as bp
import allure
from urls import *


class BasePage:
    
    def __init__(self, driver):

        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def click_element(self, element):
        self.driver.find_element(*element).click()

    def send_keys_to_element(self, element, keys):
        self.driver.find_element(*element).send_keys(keys)

    def find_the_element(self, element):
        return self.driver.find_element(*element)

    def get_text(self, element):
        return self.driver.find_element(*element).text

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        
    @allure.step('Ожидание открытия нового окна')
    def wait_for_new_window(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.number_of_windows_to_be(2))

    @allure.step('Получение URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Переключение на новое окно')
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Переключение на основное окно')
    def switch_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def wait_for_element_visible(self, element):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(element))

