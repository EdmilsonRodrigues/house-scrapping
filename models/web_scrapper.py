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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def open(self):
        self.driver.get(self.url)

    def __enter__(self):
        self.open()

    def close(self):
        self.driver.quit()

    def __exit__(self, **kwargs):
        self.close()

    def test_scraping(self):
        time.sleep(5)
        titles = self.driver.find_elements(By.TAG_NAME, "h2")
        for title in titles:
            print(title.text.strip())



if __name__ == "__main__":
    with WebScrapper("https://reva.immo/en/") as scrapper:
        scrapper.test_scraping()

