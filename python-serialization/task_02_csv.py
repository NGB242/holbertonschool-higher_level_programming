#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        """
        Open the CSV file and read the data
        """
        with open(csv_filename, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            """
            Convert each row into a dictionary and add it to a list
            """
            data = [row for row in csv_reader]

        """
        Serialize the list of dictionaries to JSON format
        """
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        """
        Handle the case where the CSV file is not found
        """
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        """
        Handle any other exceptions that may occur
        """
        print(f"An error occurred: {e}")
        return False
