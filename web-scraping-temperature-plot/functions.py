import requests
import selectorlib
import datetime
import time
import sqlite3

connection = sqlite3.connect("./temperatures.db")

URL = "https://programmer100.pythonanywhere.com/"


def scrape(url):
    response = requests.get(url)
    source = response.text
    
    return source


def extract_temperature(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]

    return value


def write_temperature(data):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures VALUES (?,?)", data)
    connection.commit()


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        date_and_time = datetime.datetime.now()
        dt_string = date_and_time.strftime("%Y-%m-%d-%H-%M-%S")
        temperature = extract_temperature(scraped)
        data = f"{dt_string},{temperature}".split(',')
        
        write_temperature(data)
        time.sleep(10)
