from selenium.webdriver.common.by import By
from general import constants
from setup.basepage import BasePage
from Selectors.selector import Elements
import pytest


class TestLogout(BasePage):
    @pytest.fixture()
    def login(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(constants.pause)
        self.driver.get(constants.API)
        email_input = self.driver.find_element(By.CSS_SELECTOR, Elements.email_address)
        email_input.send_keys(constants.META_EMAIL)
        password_input = self.driver.find_element(By.CSS_SELECTOR, Elements.password)
        password_input.send_keys(constants.META_PASSWORD)
        self.driver.find_element(By.XPATH, Elements.login_button).click()
        yield
        self.driver.close()

    def test_meta_logout(self, login):
        self.driver.find_element(By.CSS_SELECTOR, Elements.drop_down).click()
        self.driver.find_element(By.XPATH, Elements.logout)
