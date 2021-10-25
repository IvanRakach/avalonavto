import requests
from bs4 import BeautifulSoup
# from django.core.management.base import BaseCommand


URL = "https://av.by/company/1726505/cars"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/92.0.4515.131 Safari/537.36',
           'accept': '*/*'}
HOST = 'https://av.by'  # "/" - если будет нужно, то нужно подставить
FILE = 'avalonauto_cars.csv'


def get_html_auto(url, params=None):
    r = requests.get(url, params=params, headers=HEADERS)
    return r


def multiple_space_replace(target_str, replace_values):  # # Функция для замены нескольких значений
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str


def get_content_auto(html):
    soup = BeautifulSoup(html, 'html.parser')

    photos = soup.find_all('div', attrs={"class": "listing-item__photo"})
    avalon_cars_photo = []

    for img in photos:
        avalon_cars_photo.append({
            'image': img.find('img').get('data-src'),
        })
    # print('avalon_cars_photo:', avalon_cars_photo)

    title_link = soup.find_all('a', attrs={"class": "listing-item__link"}, href=True)
    avalon_cars = []
    for i in title_link:
        avalon_cars.append({
            'title': i.find('span', class_='link-text').get_text(strip=True),
            'link': i['href'],  # HOST +
        })

    region_param = soup.find_all('div', attrs={"class": "listing-item__info"})
    avalon_cars_region = []
    for region in region_param:
        avalon_cars_region.append({
            'location': region.find('div', class_='listing-item__location').get_text(strip=True),
        })

    auto_params = soup.find_all('div', attrs={"class": "listing-item__params"})
    avalon_cars_2 = []
    for p in auto_params:
        if p.find('div').find_next('div').get_text(strip=True)[0:7] == "автомат":
            eng_vol = p.find('div').find_next('div').get_text(strip=True)[8:11]
        else:
            eng_vol = p.find('div').find_next('div').get_text(strip=True)[9:12]

        if p.find('div').find_next('div').get_text(strip=True)[0:7] == "автомат":
            fuel_type = p.find('div').find_next('div').get_text(strip=True)[14:21]
        else:
            fuel_type = p.find('div').find_next('div').get_text(strip=True)[15:22]

        car_mileage = p.find('div').find_next('div').find_next('div').get_text(strip=True)
        if "\u2009" not in car_mileage and "\xa0" not in car_mileage:
            car_mileage = p.find('div').find_next('div').find_next('div').get_text(strip=True)

        elif "\u2009" in car_mileage or "\xa0" in car_mileage:
            del_spaces = {"\u2009": " ", "\xa0": " "}
            car_mileage = p.find('div').find_next('div').find_next('div').get_text(strip=True)
            car_mileage = multiple_space_replace(car_mileage, del_spaces)

        avalon_cars_2.append({
            'release_year': p.find('div').get_text(strip=True)[0:4],
            'transmission': p.find('div').find_next('div').get_text(strip=True)[0:3] + ".",  # &nbsp; - неразрывн пробел
            'eng_vol': eng_vol,
            'fuel_type': fuel_type,
            'car_mileage': car_mileage,  # &thinsp; (\u2009) ---  \xa0км
        })

    auto_prices = soup.find_all('div', attrs={"class": "listing-item__prices"})
    avalon_cars_3 = []
    for price in auto_prices:

        auto_price_byn = price.find('div', class_='listing-item__price').get_text(strip=True)
        if "\u2009" not in auto_price_byn and "\xa0" not in auto_price_byn:
            auto_price_byn = price.find('div', class_='listing-item__price').get_text(strip=True)

        elif "\u2009" in auto_price_byn or "\xa0" in auto_price_byn:
            del_spaces = {"\u2009": " ", "\xa0": " "}
            auto_price_byn = price.find('div', class_='listing-item__price').get_text(strip=True)
            auto_price_byn = multiple_space_replace(auto_price_byn, del_spaces)

        auto_price_usd = price.find('div', class_='listing-item__priceusd').get_text(strip=True)
        if "\u2009" not in auto_price_usd and "\xa0" not in auto_price_usd:
            auto_price_usd = price.find('div', class_='listing-item__priceusd').get_text(strip=True)

        elif "\u2009" in auto_price_usd or "\xa0" in auto_price_usd:
            del_spaces = {"\u2009": " ", "\xa0": " "}
            auto_price_usd = price.find('div', class_='listing-item__priceusd').get_text(strip=True)[1:]
            auto_price_usd = multiple_space_replace(auto_price_usd[1:], del_spaces)

        avalon_cars_3.append({
            'auto_price_byn': auto_price_byn,
            'auto_price_usd': auto_price_usd,
        })

    pre_pre_pre_total_list_avalon_cars = [{**x, **y} for x, y in zip(avalon_cars_photo, avalon_cars)]
    pre_pre_total_list_avalon_cars = [{**x, **y} for x, y in zip(pre_pre_pre_total_list_avalon_cars,
                                                                 avalon_cars_region)]
    pre_total_list_avalon_cars = [{**x, **y} for x, y in zip(pre_pre_total_list_avalon_cars, avalon_cars_2)]
    total_list_avalon_cars = [{**x, **y} for x, y in zip(pre_total_list_avalon_cars, avalon_cars_3)]

    # print("avalon_cars:", avalon_cars)
    # print("avalon_cars:", len(avalon_cars))
    # print("avalon_cars_2:", avalon_cars_2)
    # print("avalon_cars_2:", len(avalon_cars_2))
    # print("avalon_cars_3:", avalon_cars_3)
    # print("avalon_cars_3:", len(avalon_cars_3))

    # print("pre_total_list_avalon_cars:", pre_total_list_avalon_cars)
    # print("pre_total_list_avalon_cars:", len(pre_total_list_avalon_cars))
    # print("total_list_avalon_cars:", total_list_avalon_cars)
    # print("total_list_avalon_cars:", len(total_list_avalon_cars))

    return total_list_avalon_cars


def parse():
    html = get_html_auto(URL)
    if html.status_code == 200:
        # print(html.text)
        # print("html.status_code:", html.status_code)
        avalon_cars = get_content_auto(html.text)
        # print("avalon_cars :", avalon_cars)

        # save_file(avalon_cars, FILE)
        print(f'Получено {len(avalon_cars)} автомобилей.')  # выводим количество авто - не забыть убрать
        # os.startfile(FILE)
    else:
        print('html.status_code != 200 - Error!')


parse()
