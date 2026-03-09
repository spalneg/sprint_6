import pytest
from selenium import webdriver
from pages.main_page import MainPage
import allure
from data import *


class TestQuestionList:

    @allure.title('Проверка корректности отображения ответов на "Вопросы о важном" по клику на вопрос') 
    @allure.description('Поиск и клик по всем вопросам раздела "Вопросы о важном" на главной странице с проверкой видимости и текста ответов')
    @pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_question_answer_opens(self, driver, index):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.scroll_to_questions(index)
        main_page.click_questions(index)
        main_page.wait_answers_loading(index)
        assert main_page.check_answers_visible(index), f"Ответ на вопрос {index + 1} не отображается после клика"
        text = main_page.get_answer_text(index)
        assert text == expected_answers[index], f"Вопрос {index + 1}: ожидался текст: {expected_answers[index]}, получен: {text}"   
