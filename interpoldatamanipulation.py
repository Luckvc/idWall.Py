import requests
import json

def datainterpol():
    response = requests.get('https://ws-public.interpol.int/notices/v1/red?page=2&resultPerPage=200')
    data = response.json()

    newData = {
        'wanted' :[]
    }




    for item in data['_embedded']['notices']:
        firstName = str(item['forename'])
        lastName = str(item['name'])
        dateOfBirth = str(item['date_of_birth'])
        nationalities = str(item['nationalities'])

        link = item['_links']['self']['href']

        response = requests.get(link)
        moreData = response.json()
        gender = moreData['sex_id']
        crimes = []
        wantedIn = []

        for item in moreData['arrest_warrants']:
            crimes.append(item['charge'])
            wantedIn.append(item['issuing_country_id'])


        newWanted = {
            'firstName' :firstName,
            'lastName' :lastName,
            'dateOfBirth' :dateOfBirth,
            'nationalities' :nationalities,
            'gender' :gender,
            'crimes' :str(crimes),
            'wantedIn' :str(wantedIn)
        }

        newData['wanted'].append(newWanted)


    with open('datareadyinterpol.json', 'w') as file:
        json.dump(newData, file, indent=2)
        print("Success")

