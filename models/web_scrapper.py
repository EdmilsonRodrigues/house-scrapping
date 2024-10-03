from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class WebScrapper:
    def __init__(self, url: str) -> None:
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument("--headless")
        # self.options.add_argument("--no-sandbox")
        # self.options.add_argument("--disable-dev-shm-usage")
        self.url = url
        service = Service("/usr/bin/chromedriver")
        self.driver = webdriver.Chrome(service=service, options=self.options)

    def open(self):
        self.driver.get(self.url)

    def __enter__(self):
        self.open()
        return self

    def close(self):
        self.driver.quit()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False

    def scrape_rena_immo(self):
        time.sleep(10)
        print("Success")



if __name__ == "__main__":
    url = "https://reva.immo/en/"
    with WebScrapper(url) as scrapper:
        scrapper.scrape_rena_immo()
