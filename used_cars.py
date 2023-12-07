import requests
from bs4 import BeautifulSoup
import regex as re

for i in range(2,3195):
    url ='https://www.pakwheels.com/used-cars/search/-/?page='+str(i)
    webpage = requests.get(url).text

    soup = BeautifulSoup(webpage, 'html.parser')
    cars_featured = soup.find_all('li', class_ = 'classified-listing featured-listing')

    # Regular Expression Patterns
    pattern = r'(.*?)(?:\b\d{4}\b|$)'
    model_pattern = r'^([^\d]+)'
    details_pattern = r'\b\d{4}\b(.*?)$'
    man_pattern = r'^(\w+)'
    var_pattern = r'\b\w+\s(.*)'

    for car in cars_featured:
        # Finding the right stuff through patterns
        title = car.find('h3').text.strip()
        model_match = re.search(model_pattern, title)
        car_name = model_match.group(1).strip() if model_match else ''
        details_match = re.search(details_pattern, title)
        details = details_match.group(1).strip() if details_match else ''
        man_match = re.search(man_pattern, title)
        manufacturer = man_match.group(1) if man_match else ''
        var_match = re.search(var_pattern, car_name)
        variant = var_match.group(1) if var_match else ''
    
        location = car.find('ul', class_ = 'list-unstyled search-vehicle-info fs13').text.strip()
        price = car.find('div', class_ = 'price-details generic-dark-grey').text.strip()
        data1 = car.find('ul', class_ = 'list-unstyled search-vehicle-info-2 fs13').text.strip().split()
        model = data1[0]
        distance_travelled = data1[1].replace(',','')
        fuel_type = data1[3]
        engine_capacity = data1[4]
        transmission = data1[6]
        featured = 'Yes'

        # Removing For sale
        details = details.replace('for Sale',"")

        with open('used_cars.csv', 'a') as f:
            f.write(f'{manufacturer},{variant},{details},{location},{model},{distance_travelled},{fuel_type},{engine_capacity},{transmission},{featured},{price}\n')

    cars_not_featured = soup.find_all('li', class_ = 'classified-listing')
    for car in cars_not_featured:
        # Finding the right stuff through patterns
        title = car.find('h3').text.strip()
        model_match = re.search(model_pattern, title)
        car_name = model_match.group(1).strip() if model_match else ''
        details_match = re.search(details_pattern, title)
        details = details_match.group(1).strip() if details_match else ''
        man_match = re.search(man_pattern, title)
        manufacturer = man_match.group(1) if man_match else ''
        var_match = re.search(var_pattern, car_name)
        variant = var_match.group(1) if var_match else ''
    
        location = car.find('ul', class_ = 'list-unstyled search-vehicle-info fs13').text.strip()
        price = car.find('div', class_ = 'price-details generic-dark-grey').text.strip()
        data1 = car.find('ul', class_ = 'list-unstyled search-vehicle-info-2 fs13').text.strip().split()
        model = data1[0]
        distance_travelled = data1[1].replace(',','')
        fuel_type = data1[3]
        engine_capacity = data1[4]
        transmission = data1[6]
        featured = 'No'

        # Removing For sale
        details = details.replace('for Sale',"")

        with open('used_cars.csv', 'a') as f:
            f.write(f'{manufacturer},{variant},{details},{location},{model},{distance_travelled},{fuel_type},{engine_capacity},{transmission},{featured},{price}\n')

