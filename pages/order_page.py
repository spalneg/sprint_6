from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators as op
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)


    
    @allure.step('Загрузка страницы оформления заказа')
    def wait_order_page_loading(self):
        self.wait_for_element_visible(op.next_button)

    @allure.step('Ввод в поле "Имя" имени {name}')
    def set_name(self, name):
        self.send_keys_to_element(op.name_field, name)

    @allure.step('Ввод в поле "Фамилия" фамилии {surname}')
    def set_surname(self, surname):
        self.send_keys_to_element(op.surname_field, surname)

    @allure.step('Ввод в поле "Адрес" адреса {address}')
    def set_address(self, address):
        self.send_keys_to_element(op.address_field, address)

    @allure.step('Ввод в поле "Метро" станции {metro}')
    def set_metro(self, metro):
        self.send_keys_to_element(op.metro_field, metro)
        self.click_element(op.metro_list)
    
    @allure.step('Ввод в поле "Телефон" номера {phone}')
    def set_phone(self, phone):
        self.send_keys_to_element(op.phone_field, phone)
    
    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.click_element(op.next_button)

    @allure.step('Ожидание загрузки следующих полей ввода')
    def wait_for_next_fields(self):
        self.wait_for_element_visible(op.date_field)    
    
    @allure.step('Ввод в поле "Дата" даты {date}')
    def set_date(self, date):
        self.send_keys_to_element(op.date_field, date) 
        self.send_keys_to_element(op.date_field, Keys.ESCAPE)    

    @allure.step('Ввод в поле "Срок аренды" срока {duration}')
    def set_duration(self, duration):
        self.click_element(op.duration_field)
        self.click_element(op.duration_option(duration))
    
    @allure.step('Клик по кнопке заказа')
    def click_order_button(self):
        self.click_element(op.order_submit_button)
    
    @allure.step('Ожидания окна подтверждения заказа')
    def wait_for_confirmation_popup(self):
        self.wait_for_element_visible(op.confirm_yes_button)

    @allure.step('Клик по кнопке подтверждения заказа')
    def click_confirm_button(self):
        self.click_element(op.confirm_yes_button)

    @allure.step('Ожидание информаци о статусе заказе')
    def wait_for_order_confirm(self):
        self.wait_for_element_visible(op.order_info)

    @allure.step('Получение сообщения о статусе заказа')
    def get_order_status(self):
        return self.find_the_element(op.order_info).text       

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

