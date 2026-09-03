"""
Report Generation Functions for Flight Operations

This module contains functions for reading, processing, and reporting on
military flight operations data. Students will implement these functions
to practice file I/O, data manipulation, and report generation.
"""

import csv


def read_csv_file(filepath):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    """
    # Create an empty list to store the records
    data = []

    # Open the CSV file
    with open(filepath, 'r') as file:
        # DictReader turns each row into a dictionary
        reader = csv.DictReader(file)

        # Add each row to our data list
        for row in reader:
            data.append(row)

    return data


def count_records(data_list):
    """Counts the number of records in a dataset."""
    # len() tells us how many items are in the list
    return len(data_list)


def get_unique_values(data_list, field_name):
    """Gets all unique values for a specific field in the dataset."""
    # A set automatically removes duplicates
    unique_values = set()

    # Look through every record
    for record in data_list:
        unique_values.add(record[field_name])

    # Convert the set into a sorted list
    return sorted(list(unique_values))


def filter_by_field(data_list, field_name, field_value):
    """Filters records where a specific field matches a given value."""
    # Create an empty list for matching records
    filtered_data = []

    # Look through every record
    for record in data_list:
        # Check if the field matches what we are looking for
        if record[field_name] == field_value:
            filtered_data.append(record)

    return filtered_data


def calculate_total(data_list, field_name):
    """Calculates the sum of a numeric field across all records."""
    # Start the total at zero
    total = 0

    # Loop through each record
    for record in data_list:
        # CSV numbers are strings, so convert them to floats
        total = total + float(record[field_name])

    return total


def calculate_average(data_list, field_name):
    """Calculates the average value of a numeric field."""
    # Get the number of records
    count = count_records(data_list)

    # Prevent dividing by zero if the list is empty
    if count == 0:
        return 0

    # Get the total using our calculate_total function
    total = calculate_total(data_list, field_name)

    # Average is total divided by count
    average = total / count

    return average


def find_record_by_id(data_list, id_field, id_value):
    """Finds a specific record by its ID field."""
    # Look through every record
    for record in data_list:
        # Check if the ID matches
        if record[id_field] == id_value:
            return record

    # Return None if nothing was found
    return None


def join_data(primary_list, secondary_list, primary_key, foreign_key):
    """
    Joins two datasets together based on matching key fields.
    Similar to a SQL JOIN.
    """
    # Create a lookup dictionary
    lookup = {}

    # Build the lookup dictionary using the secondary data
    for record in secondary_list:
        lookup[record[foreign_key]] = record

    # This will hold the joined records
    joined_data = []

    # Loop through the primary data
    for record in primary_list:
        # Make a copy so we do not change the original record
        combined_record = record.copy()

        # Get the value that we want to match
        key_value = record[primary_key]

        # Check if that value exists in the lookup dictionary
        if key_value in lookup:
            # Add the secondary record information
            combined_record.update(lookup[key_value])

        # Add the combined record to our results
        joined_data.append(combined_record)

    return joined_data


def write_report_to_file(filepath, content):
    """Writes a text report to a file."""
    # Open the file in write mode
    with open(filepath, 'w') as file:
        # Write the report content
        file.write(content)


def format_header(title):
    """Creates a formatted header for reports."""
    # Create the top and bottom border
    line = "=" * 60

    # Center the title between the lines
    header = line + "\n"
    header = header + title.center(60) + "\n"
    header = header + line

    return header


# Testing functions
if __name__ == '__main__':
    print("Testing report functions...")

    # Test read_csv_file
    pilots = read_csv_file('data/pilots.csv')
    print(f"Loaded {len(pilots)} pilots")

    # Test count_records
    print(f"Pilot count: {count_records(pilots)}")

    # Test get_unique_values
    squadrons = get_unique_values(pilots, 'squadron')
    print(f"Squadrons: {squadrons}")

    # Test filter_by_field
    vfa_41_pilots = filter_by_field(pilots, 'squadron', 'VFA-41')
    print(f"VFA-41 pilots: {len(vfa_41_pilots)}")

    # Test find_record_by_id
    pilot = find_record_by_id(pilots, 'pilot_id', 'P001')
    print(f"P001: {pilot}")
