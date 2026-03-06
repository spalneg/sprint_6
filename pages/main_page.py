from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators as mp
from locators.base_page_locators import BasePageLocators as bp
import allure


class MainPage:
    
    def __init__(self, driver):
        
        self.driver = driver
        self.questions = [mp.question_1, mp.question_2, mp.question_3, mp.question_4, mp.question_5, mp.question_6, mp.question_7, mp.question_8]
        self.answers = [mp.answer_1, mp.answer_2, mp.answer_3, mp.answer_4, mp.answer_5, mp.answer_6, mp.answer_7, mp.answer_8]

    @allure.step('Открыть главную страницу')       
    def open_main_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

    @allure.step('Прокрутка страницы до проверяемого вопроса')
    def scroll_to_questions(self, index):
        element = self.driver.find_element(*self.questions[index])
        self.driver.execute_script("arguments[0].scrollIntoView();", element) 

    @allure.step('Клик по вопросу')
    def click_questions(self, index):
        self.driver.find_element(*self.questions[index]).click()

    @allure.step('Ожидание загрузки вопросов')
    def wait_answers_loading(self, index):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.answers[index])) 

    @allure.step('Проверка видимости ответа')
    def check_answers_visible(self, index):
        return self.driver.find_element(*self.answers[index]).is_displayed()

    @allure.step('Выбор кнопки "Заказать" для начала тестового сценария')
    def choose_order_button(self, order_button):
        if order_button == "main":
            element = self.driver.find_element(*mp.main_order_button)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)           
            self.driver.find_element(*mp.main_order_button).click()
        elif order_button == "base":
            self.driver.find_element(*bp.base_order_button).click()