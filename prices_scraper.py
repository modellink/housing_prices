import pandas
import pandas as pd
from typing import List
import requests
from bs4 import BeautifulSoup


def get_house_price(house):
    return house.find('p', {'class': 'exchanged-price specified'}).text.strip()[5:]


def scrape_content(url: str):
    df = pd.DataFrame(columns=['price'])
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    houses = soup.findAll('li', {'class': 'listing'})
    with open('houses.csv', 'w') as file:
        file.write('prices;\n')
        for house in houses:
            file.write(f'{get_house_price(house)};\n')


def get_scraped_content() -> pd.DataFrame:
    return pandas.read_csv('houses.csv', sep=';')


if __name__ == '__main__':
    scrape_content('https://www.realtor.com/international/il/')
    print(get_scraped_content())
