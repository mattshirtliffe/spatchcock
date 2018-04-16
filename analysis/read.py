import csv
import datetime
import json

# play time!
# how would I convert this file into a .json file?

def convert_crime_data_to_json(crimes):
    return json.dumps({"crimes":crimes})

def create_json_file(filename,data):
    filename +='.json'
    with open(filename,"w") as f:
        f.write(data)
    f.close()

def create_csv_file_from_dict(filename,data):
    filename +='.csv'
    with open(filename, "w") as f:
        csv_writer = csv.writer(f, delimiter=',')
        for crime in data:
            row = []
            for k, v in crime.items():
                row.append(v)
            csv_writer.writerow(row)
    f.close()

def clean_date(month_str):
    year, month = month_str.split('-')
    year = int(year)
    month = int(month)
    date = datetime.date(year=year, month=month, day=1)
    return date.strftime('%Y-%m-%d')

def clean_crime_rows(data_crime):
    crimes = []
    for row in data_crime:
        if row["crime_id"] and row["outcome_status"]:
            row["month"] = clean_date(row["month"])
            crimes.append(row)
    return crimes

def get_crime_data_from_csv():
    crimes = []
    with open('crime_data.csv', 'r') as csvfile:
        crime_reader = csv.DictReader(csvfile, delimiter=',')
        for row in crime_reader:
            crimes.append(row)
    csvfile.close()
    return crimes

if __name__ == '__main__':
    # get all values in csv
    dirty_crimes = get_crime_data_from_csv()

    # clean values
    cleaned_crimes = clean_crime_rows(dirty_crimes)
    create_csv_file_from_dict('clean_crime_data',cleaned_crimes)
    print(cleaned_crimes)

    # print(crimes)
    # crimes = convert_crime_data_to_json(crimes)
    # create_json_file('crime_data',crimes)
    # print(row["category"])
    # crime_categories.append(row["category"])
    # crime_categories = set(crime_categories)
    # print(crime_categories)
    # print(len(crime_categories))
