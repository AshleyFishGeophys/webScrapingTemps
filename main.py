from functions import scrape, extract, store, read, get_utc_time


URL = "https://programmer100.pythonanywhere.com/"

time = get_utc_time()
scraped = scrape(URL)
extracted = extract(scraped)
content = read()
store(content)

