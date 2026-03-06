from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators as op
import allure


class OrderPage:

    def __init__(self, driver):

        self.driver = driver
    
    @allure.step('Загрузка страницы оформления заказа')
    def wait_order_page_loading(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(op.next_button)) 

    @allure.step('Ввод в поле "Имя" имени {name}')
    def set_name(self, name):
        self.driver.find_element(*op.name_field).send_keys(name)

    @allure.step('Ввод в поле "Фамилия" фамилии {surname}')
    def set_surname(self, surname):
        self.driver.find_element(*op.surname_field).send_keys(surname)

    @allure.step('Ввод в поле "Адрес" адреса {address}')
    def set_address(self, address):
        self.driver.find_element(*op.address_field).send_keys(address)

    @allure.step('Ввод в поле "Метро" станции {metro}')
    def set_metro(self, metro):
        self.driver.find_element(*op.metro_field).send_keys(metro)
        self.driver.find_element(*op.metro_list).click()
    
    @allure.step('Ввод в поле "Телефон" номера {phone}')
    def set_phone(self, phone):
        self.driver.find_element(*op.phone_field).send_keys(phone)
    
    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.driver.find_element(*op.next_button).click()

    @allure.step('Ожидание загрузки следующих полей ввода')
    def wait_for_next_fields(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(op.date_field))    
    
    @allure.step('Ввод в поле "Дата" даты {date}')
    def set_date(self, date):
        self.driver.find_element(*op.date_field).send_keys(date) 
        self.driver.find_element(*op.date_field).send_keys(Keys.ESCAPE)    

    @allure.step('Ввод в поле "Срок аренды" срока {duration}')
    def set_duration(self, duration):
        self.driver.find_element(*op.duration_field).click()
        self.driver.find_element(*op.duration_option(duration)).click()
    
    @allure.step('Клик по кнопке заказа')
    def click_order_button(self):
        self.driver.find_element(*op.order_submit_button).click()
    
    @allure.step('Ожидания окна подтверждения заказа')
    def wait_for_confirmation_popup(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(op.confirm_yes_button)) 

    @allure.step('Клик по кнопке подтверждения заказа')
    def click_confirm_button(self):
        self.driver.find_element(*op.confirm_yes_button).click()

    @allure.step('Ожидание информаци о статусе заказе')
    def wait_for_order_confirm(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(op.order_info))

    @allure.step('Получение сообщения о статусе заказа')
    def get_order_status(self):
        return self.driver.find_element(*op.order_info).text       

    @allure.step('Заполнение формы заказа самоката с подтверждением заказа')
    def order_scooter(self, name, surname, address, metro, phone, date, duration):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.click_next_button()
        self.wait_for_next_fields()        
        self.set_date(date)
        self.set_duration(duration)
        self.click_order_button()
        self.wait_for_confirmation_popup()
        self.click_confirm_button()
        self.wait_for_order_confirm()

