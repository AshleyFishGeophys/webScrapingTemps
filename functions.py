import csv
import requests
import selectorlib
import time
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Establish a connection to the sqlite3 db
connection = sqlite3.connect("temps.db")

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

def store(date, temp):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?)", (date, temp))
    print("stored date and temp: ", date, temp)
    connection.commit()

def get_from_db():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events")
    data = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    split_data = {column: [] for column in column_names}
    for row in data:
        for i, value in enumerate(row):
            column_name = column_names[i]
            split_data[column_name].append(value)
    temps = split_data["temperature"]
    dates = split_data["date"]
    return dates, temps


if __name__ == "__main__":
    while True:
        date = get_utc_time()
        scraped = scrape(URL)
        extracted = extract(scraped)
        store(date, extracted)
        time.sleep(2)

    # dates, temps = get_from_db()
