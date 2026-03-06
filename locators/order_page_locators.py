from selenium.webdriver.common.by import By


class OrderPageLocators:
    name_field = [By.XPATH, '//input[@placeholder="* Имя"]']
    surname_field = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    address_field = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_field = [By.XPATH, '//input[@placeholder="* Станция метро"]']
    metro_list = [By.CLASS_NAME, 'select-search__select']
    phone_field = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    next_button = [By.CLASS_NAME, 'Button_Middle__1CSJM']
    date_field = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    duration_field = [By.CLASS_NAME, 'Dropdown-placeholder']
    @staticmethod
    def duration_option(duration):
        return [By.XPATH, f"//div[text()='{duration}']"]
    order_submit_button = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']
    confirm_yes_button = [By.XPATH, '//button[text()="Да"]']
    order_info = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']


