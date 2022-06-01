from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from startup.start_page import Start
from general import constants


class BasePage(Start):

    def opera(self):
        self.option1 = Options
        self.option1.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.service = Service(constants.sever_path)
        self.driver = webdriver.Chrome(executable_path=constants.sever_path, chrome_options=self.option1)
