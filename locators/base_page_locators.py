from selenium.webdriver.common.by import By


class BasePageLocators:
    base_order_button = [By.CLASS_NAME, 'Button_Button__ra12g']
    logo_button = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    yandex_button = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    dzen_locator = [By.XPATH, '//a[@aria-label="Логотип Бренда"]']