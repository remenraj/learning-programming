#! /usr/bin/env python3
# Program to extract squirrel data from the census data(fur color count) from the census data
# and saves it in a csv file

import pandas, math

# File directories
CENSUS_DATA_FILE_DIR = r"learning-programming\Python\21-50\30-the-great-squirrel-census-data-analysis-2018\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
FUR_COLOR_DATA_FILE_DIR = r"learning-programming\Python\21-50\30-the-great-squirrel-census-data-analysis-2018\fur_color_data.csv"


def squirrel():
    """Extracts squirrel data(fur color count) from the census data and saves it in a csv file"""
    # creating DataFrame
    squirrel_data = pandas.read_csv(CENSUS_DATA_FILE_DIR)

    # extracting Primary Fur Color Series from the DataFrame
    fur_color = squirrel_data["Primary Fur Color"]

    # counting the total colored squirrels
    gray_count = len(squirrel_data[fur_color == "Gray"])
    black_count = len(squirrel_data[fur_color == "Black"])
    cinnamon_count = len(squirrel_data[fur_color == "Cinnamon"])

    # creating dictionary
    fur_color_dict = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [gray_count, cinnamon_count, black_count],
    }

    # converting dictionary to DataFrame
    fur_color_df = pandas.DataFrame(data=fur_color_dict)

    # saving DataFrame into a csv file
    fur_color_df.to_csv(path_or_buf=f"{FUR_COLOR_DATA_FILE_DIR}\\fur_color_data.csv")


if __name__ == "__main__":
    squirrel()
