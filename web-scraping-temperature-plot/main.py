import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/"

def scrape(url):
    response = requests.get(url)
    source = response.text
    
    return source


def extract_temperature(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    
    return value

if __name__ == "__main__":
    scraped = scrape(URL)
    temperature = extract_temperature(scraped)
    print(temperature)
