import requests

url_template = 'http://wttr.in/{}'
payload = {'nTqm': '', 'lang': 'ru'}
locations = ['London', 'svo', 'Череповец']

for location in locations:
    try:
        url = url_template.format(location)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from server:\n{0}".format(error))
