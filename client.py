
# a commandline tool that reads data from csv file and perform http request to restful api
import csv
import requests

with open('crime_data.csv', 'r') as csvfile:
    crime_reader = csv.DictReader(csvfile, delimiter=',')
    for row in crime_reader:
        r = requests.post('http://127.0.0.1:5000/crime', json=row)
        print(r.status_code)
        print(r.text)