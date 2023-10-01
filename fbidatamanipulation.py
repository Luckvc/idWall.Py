import json
import requests

response = requests.get('https://api.fbi.gov/@wanted?pageSize=200&page=1')

data = response.json()

newData = {
    'wanted' :[]
}




for item in data['items']:
    name = str(item['title'])
    dateOfBirth = str(item['dates_of_birth_used'])
    nationalities = str(item['nationality'])
    gender = str(item['sex'])
    crimes = str(item['description'])



    newWanted = {
        'name' :name,
        'dateOfBirth' :dateOfBirth,
        'nationalities' :nationalities,
        'gender' :gender,
        'crimes' :crimes,
    }

    newData['wanted'].append(newWanted)


with open('datareadyfbi.json', 'w') as file:
    json.dump(newData, file)
