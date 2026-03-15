from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

import time
import logging


def start_driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    return driver


def infinite_scroll(driver):

    last_height = driver.execute_script(
        "return document.body.scrollHeight"
    )

    while True:

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        time.sleep(2)

        new_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        if new_height == last_height:
            break

        last_height = new_height


def scrape_quotes(driver):

    quotes = driver.find_elements(By.CLASS_NAME, "quote")

    data = []

    for q in quotes:

        text = q.find_element(By.CLASS_NAME, "text").text
        author = q.find_element(By.CLASS_NAME, "author").text

        tags = [t.text for t in q.find_elements(By.CLASS_NAME, "tag")]

        data.append({
            "quote": text,
            "author": author,
            "tags": ", ".join(tags)
        })

    return data