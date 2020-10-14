import os
import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_nutritives():
    """ФУНКЦИЯ ПАРСЕНГА ДАННЫХ С САЙТА"""
    html = get_html(os.getenv('SITE_ADDRESS'))
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        category = soup.findAll('table', class_="energy-res-tb")
        result = []
        results = []
        for item in category:
            products = item.findAll('tr')
            result.append(products)
            for nutritives in products:
                for i in nutritives:
                    name = nutritives.find('th').text
                    fats = nutritives.find('a', id="fat").text
                    calories = nutritives.find('a', id="calories").text
                results.append({
                    "name": name,
                    "fats": fats,
                    "calories": calories
                })
        return results


def save(results, path):
    """ФУНКЦИЯ ЗАПИСИ СПАРСЕННЫХ ДАННЫХ В CSV ФАЙЛ"""
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Количество на 100г продукта:', 'Жиры, г', 'Ккал'))
        for iter in results:
            writer.writerow((iter['name'], iter['fats'], iter['calories']))


if __name__ == "__main__":
    parse = get_nutritives()
    save(parse, 'calories.csv')
