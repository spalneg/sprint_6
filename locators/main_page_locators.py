from selenium.webdriver.common.by import By


class MainPageLocators:
        question_1 = [By.ID, 'accordion__heading-0']
        question_2 = [By.ID, 'accordion__heading-1']
        question_3 = [By.ID, 'accordion__heading-2']
        question_4 = [By.ID, 'accordion__heading-3']
        question_5 = [By.ID, 'accordion__heading-4']
        question_6 = [By.ID, 'accordion__heading-5']
        question_7 = [By.ID, 'accordion__heading-6']
        question_8 = [By.ID, 'accordion__heading-7'] 
        answer_1 = [By.XPATH, '//*[@id ="accordion__panel-0"]/p']
        answer_2 = [By.XPATH, '//*[@id ="accordion__panel-1"]/p']
        answer_3 = [By.XPATH, '//*[@id ="accordion__panel-2"]/p']
        answer_4 = [By.XPATH, '//*[@id ="accordion__panel-3"]/p']
        answer_5 = [By.XPATH, '//*[@id ="accordion__panel-4"]/p']
        answer_6 = [By.XPATH, '//*[@id ="accordion__panel-5"]/p']
        answer_7 = [By.XPATH, '//*[@id ="accordion__panel-6"]/p']
        answer_8 = [By.XPATH, '//*[@id ="accordion__panel-7"]/p']
        main_order_button = [By.CLASS_NAME, 'Button_Middle__1CSJM']  