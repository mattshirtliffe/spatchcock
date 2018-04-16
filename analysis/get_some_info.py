import csv


def get_crime_data_from_csv():
    crimes = []
    with open('clean_crime_data.csv', 'r') as csvfile:
        crime_reader = csv.DictReader(csvfile, delimiter=',')
        for row in crime_reader:
            crimes.append(row)
    csvfile.close()
    return crimes

def get_categories(crimes):
    crime_categories = []
    # crime_id, month, latitude, longitude, location, category, outcome_status
    for crime in crimes:
        crime_category = crime['category']
        crime_categories.append(crime_category)

    crime_categories = set(crime_categories)
    print(crime_categories)
    print(len(crime_categories))

def get_number_of_crimes_by_category(crimes):

    crime_by_category = {}

    for crime in crimes:
        if crime['category'] in crime_by_category.keys():
            crime_by_category[crime['category']] += 1
        else:
            crime_by_category[crime['category']] = 1
    print(crime_by_category)

if __name__ == '__main__':
    # get all values in csv
    crimes = get_crime_data_from_csv()
    get_number_of_crimes_by_category(crimes)
    get_categories(crimes)


