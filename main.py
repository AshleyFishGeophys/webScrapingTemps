from functions import scrape, extract, store, get_utc_time
import time

URL = "https://programmer100.pythonanywhere.com/"

while True:
    date = get_utc_time()
    scraped = scrape(URL)
    extracted = extract(scraped)
    store(date, extracted)
    time.sleep(2)
