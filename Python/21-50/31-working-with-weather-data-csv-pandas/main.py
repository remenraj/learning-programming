# Program exploring csv file and pandas module

import csv, pandas


CSV_FILE_DIR = r"Workspace\100-days-of-code\day-25\working-with-weather-data-csv-pandas"
NEW_CSV_FILE_DIR = (
    r"Workspace\100-days-of-code\day-25\working-with-weather-data-csv-pandas"
)


def csvfile():

    #### Method 1 using files ####
    # extract data from csv file and convert it into a list cotaining list of data
    # data = []
    # with open(CSV_FILE_DIR) as csvfile:
    #     data = csvfile.readlines()
    # for i in range(len(data)):
    #     item = data[i]
    #     data[i] = item.strip().split(",")

    #### Method 2 using csv module ####
    # extracting temperature from csv file, convert it into an integer and store it in a list
    # temperatures = []
    # with open(CSV_FILE_DIR) as data_file:
    #     data = csv.reader(data_file)

    #     for row in data:
    #         if row[1] == "temp":
    #             continue
    #         temperatures.append(int(row[1]))
    #         print(row)
    # print(temperatures)

    #### Method 3 using pandas module ####
    # creating dataframe
    data = pandas.read_csv(f"{CSV_FILE_DIR}\\weather_data.csv")
    print(data)

    # temperatures = data["temp"]
    print(data["temp"])

    # # creating a data dictionary
    data_dict = data.to_dict()
    print(data_dict)

    # # creating temperature list
    temperature_list = data["temp"].to_list()
    print(temperature_list)

    average_temperature = sum(temperature_list) / len(temperature_list)
    print(f"Average temperature: {average_temperature}")

    # # using pandas module
    average_temperature = data["temp"].mean()
    print(f"Average temperature: {average_temperature}")

    max_temperature = data["temp"].max()
    print(f"Maximum temperature: {max_temperature}")

    # # get data in row
    print("Monday row:")
    print(data[data.day == "Monday"])

    # # get the row where temperature is maximum
    print("Max temperature row:")
    print(data[data.temp == data.temp.max()])

    # get monday's temperature and convert it into fahrenheit
    row = data[data.day == "Monday"]
    print(row.temp)
    monday_temperature = int(row.temp)
    t_f = (9 / 5) * monday_temperature + 32
    print(t_f)

    # create a data dictionary from scratch
    data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

    # convert data dictionary into data frame
    new_data = pandas.DataFrame(data=data_dict)
    print(new_data)
    new_data.to_csv(f"{NEW_CSV_FILE_DIR}\\score_data.csv")


if __name__ == "__main__":
    csvfile()
