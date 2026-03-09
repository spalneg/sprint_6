from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators as mp
from locators.base_page_locators import BasePageLocators as bp
from pages.base_page import BasePage
import allure
from urls import *


class MainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.questions = [mp.question_1, mp.question_2, mp.question_3, mp.question_4, mp.question_5, mp.question_6, mp.question_7, mp.question_8]
        self.answers = [mp.answer_1, mp.answer_2, mp.answer_3, mp.answer_4, mp.answer_5, mp.answer_6, mp.answer_7, mp.answer_8]

    @allure.step('Открыть главную страницу')       
    def open_main_page(self):
        self.open_page(BASE_URL)

    @allure.step('Клик по логотипу Самокат')
    def click_logo_button(self):
        self.click_element(bp.logo_button)

    @allure.step('Клик по логотипу Яндекс')
    def click_yandex_button(self):
        self.click_element(bp.yandex_button)

    @allure.step('Ожидание открытия сайта Дзен')
    def wait_dzen_loading(self):
        self.wait_for_element_visible(bp.dzen_locator)

    @allure.step('Прокрутка страницы до проверяемого вопроса')
    def scroll_to_questions(self, index):
        self.wait_for_element_visible(self.questions[index])
        element = self.find_the_element(self.questions[index])
        self.scroll_to(element) 

    @allure.step('Клик по вопросу')
    def click_questions(self, index):
        self.click_element(self.questions[index])

    @allure.step('Ожидание загрузки вопросов')
    def wait_answers_loading(self, index):
        self.wait_for_element_visible(self.answers[index])

    @allure.step('Проверка видимости ответа')
    def check_answers_visible(self, index):
        return self.find_the_element(self.answers[index]).is_displayed()
    
    @allure.step('Получение текста ответа')
    def get_answer_text(self, index):
        return self.find_the_element(self.answers[index]).text
    
    @allure.step('Клик по кнопке "заказать" на главной странице')
    def click_base_order_button(self):
        self.click_element(bp.base_order_button)

    @allure.step('Выбор кнопки "Заказать" для начала тестового сценария')
    def choose_order_button(self, order_button):
        if order_button == "main":
            element = self.find_the_element(mp.main_order_button)
            self.scroll_to(element)           
            self.click_element(mp.main_order_button)
        elif order_button == "base":
            self.click_base_order_button()