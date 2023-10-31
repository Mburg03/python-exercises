import requests
import selectorlib
import datetime

URL = "https://programmer100.pythonanywhere.com/"


def scrape(url):
    response = requests.get(url)
    source = response.text
    
    return source


def extract_temperature(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    
    return value


def write_temperature(date, temperature):
    with open('./temperatures.csv', 'a') as file:
        file.write(f"{date},{temperature}" + "\n")
        

if __name__ == "__main__":
    scraped = scrape(URL)
    temperature = extract_temperature(scraped)
    date_and_time = datetime.datetime.now()
    dt_string = date_and_time.strftime("%Y-%m-%d-%H-%M-%S")
    write_temperature(dt_string, temperature)
    
