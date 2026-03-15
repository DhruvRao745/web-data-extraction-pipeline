import pandas as pd
import os
import logging

from scraper import start_driver, infinite_scroll, scrape_quotes


logging.info("Starting JS scraper")

driver = start_driver()

url = "https://quotes.toscrape.com/scroll"

driver.get(url)

infinite_scroll(driver)

data = scrape_quotes(driver)

driver.quit()

df = pd.DataFrame(data)

os.makedirs("dataset", exist_ok=True)

df.to_csv("dataset/js_quotes.csv", index=False)

df.to_json("dataset/js_quotes.json", orient="records")

logging.info(f"Scraped {len(df)} records")