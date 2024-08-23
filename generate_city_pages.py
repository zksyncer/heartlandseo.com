import csv
import os
from datetime import datetime

def create_city_page(city, state):
    with open('city-template.md', 'r') as template_file:
        template = template_file.read()
    
    replacements = {
        '[CITY]': city,
        '[STATE]': state,
        '[STATE-LOWERCASE]': state.lower(),
        '[CITY-LOWERCASE]': city.lower().replace(' ', '-'),
        '[CURRENT_YEAR]': str(datetime.now().year)
    }
    
    for old, new in replacements.items():
        template = template.replace(old, new)
    
    directory = f'cities/{state.lower()}'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    filename = f'{directory}/{city.lower().replace(" ", "-")}.md'
    with open(filename, 'w') as city_file:
        city_file.write(template)
    
    print(f"Created page for {city}, {state}")

# Read cities from CSV file
with open('missouri-kansas-cities.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row['population']) > 5000:
            create_city_page(row['city'], row['state'])

print("City pages generation complete!")
