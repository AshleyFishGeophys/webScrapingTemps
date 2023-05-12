import csv
import requests
import selectorlib
import time


URL = "https://programmer100.pythonanywhere.com/"

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temps"]
    return value

def get_utc_time():
    current_time = time.time()
    utc_time = time.gmtime(current_time)
    utc_time_str = time.strftime("%Y-%m-%d %H:%M:%S", utc_time)
    print("UTC time string:", utc_time_str)
    return utc_time_str


def store(time, extracted):
    with open("data.txt", "a") as file:
        file.write(time + "," + extracted + "\n")


def read():
    with open("data.txt", "r") as file:
        reader = csv.DictReader(file, delimiter=',', fieldnames=["date", "temperature"])

        # skips the header row
        next(reader)

        # Extract dates and temps using list comprehension
        dates = []
        temps = []
        for row in reader:
            dates.append(row["date"])
            temps.append(row["temperature"])

        return dates, temps

if __name__ == "__main__":
    time = get_utc_time()
    scraped = scrape(URL)
    extracted = extract(scraped)
    dates, temps = read()
    store(time, extracted)