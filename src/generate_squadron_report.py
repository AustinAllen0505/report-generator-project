"""
Squadron Activity Report Generator

This script demonstrates how to use the report_functions module
to generate a comprehensive squadron activity report.

Students will build this step-by-step in the assignment.
"""

import report_functions as rf


def generate_squadron_report(squadron_code, output_file):
    """
    Generates a comprehensive activity report for a specific squadron.

    Args:
        squadron_code (str): Squadron identifier (e.g., 'VFA-41')
        output_file (str): Path to save the report
    """

    # TODO: PART 1 - Load the data files

    pilots = rf.read_csv_file('data/pilots.csv')
    aircraft = rf.read_csv_file('data/aircraft.csv')
    flights = rf.read_csv_file('data/flight_logs.csv')

    print(f"Loaded {len(pilots)} pilots")
    print(f"Loaded {len(aircraft)} aircraft")
    print(f"Loaded {len(flights)} flights")


    # TODO: PART 2 - Filter data for the specified squadron

    squadron_pilots = rf.filter_by_field(
        pilots,
        'squadron',
        squadron_code
    )

    squadron_aircraft = rf.filter_by_field(
        aircraft,
        'squadron',
        squadron_code
    )

    print(
        f"Squadron {squadron_code} has "
        f"{len(squadron_pilots)} pilots"
    )


    # TODO: PART 3 - Get flights for squadron pilots

    # Make a list of pilot IDs that belong to this squadron
    pilot_ids = []

    for pilot in squadron_pilots:
        pilot_ids.append(pilot['pilot_id'])

    # Find every flight flown by one of those pilots
    squadron_flights = []

    for flight in flights:
        if flight['pilot_id'] in pilot_ids:
            squadron_flights.append(flight)

    print(
        f"Found {len(squadron_flights)} flights "
        f"for {squadron_code}"
    )


    # TODO: PART 4 - Calculate statistics

    total_flight_hours = rf.calculate_total(
        squadron_flights,
        'duration_hours'
    )

    total_missions = rf.count_records(squadron_flights)

    average_duration = rf.calculate_average(
        squadron_flights,
        'duration_hours'
    )

    # Find the different mission types
    mission_types = rf.get_unique_values(
        squadron_flights,
        'mission_type'
    )

    # Count how many missions belong to each type
    mission_counts = {}

    for mission_type in mission_types:
        matching_missions = rf.filter_by_field(
            squadron_flights,
            'mission_type',
            mission_type
        )

        mission_counts[mission_type] = len(matching_missions)


    # TODO: PART 5 - Build the report content

    report = ""

    report = report + rf.format_header(
        f"{squadron_code} SQUADRON ACTIVITY REPORT"
    )

    report = report + "\n\n"

    # Squadron overview
    report = report + rf.format_header("SQUADRON OVERVIEW")
    report = report + "\n"

    report = report + f"Squadron: {squadron_code}\n"
    report = report + f"Assigned Pilots: {len(squadron_pilots)}\n"
    report = report + f"Assigned Aircraft: {len(squadron_aircraft)}\n"


    # Pilot section
    report = report + "\n"
    report = report + rf.format_header("ASSIGNED PILOTS")
    report = report + "\n"

    for pilot in squadron_pilots:
        report = report + (
            f"{pilot['rank']} "
            f"{pilot['first_name']} "
            f"{pilot['last_name']} "
            f"\"{pilot['callsign']}\"\n"
        )


    # Aircraft section
    report = report + "\n"
    report = report + rf.format_header("ASSIGNED AIRCRAFT")
    report = report + "\n"

    for plane in squadron_aircraft:
        report = report + (
            f"{plane['aircraft_id']} - "
            f"{plane['model']} - "
            f"Tail Number: {plane['tail_number']} - "
            f"Status: {plane['status']}\n"
        )


    # Flight statistics section
    report = report + "\n"
    report = report + rf.format_header("FLIGHT STATISTICS")
    report = report + "\n"

    report = report + f"Total Missions: {total_missions}\n"
    report = report + (
        f"Total Flight Hours: {total_flight_hours:.2f}\n"
    )
    report = report + (
        f"Average Mission Duration: {average_duration:.2f} hours\n"
    )


    # Mission breakdown section
    report = report + "\n"
    report = report + rf.format_header("MISSION TYPE BREAKDOWN")
    report = report + "\n"

    for mission_type in mission_counts:
        report = report + (
            f"{mission_type}: "
            f"{mission_counts[mission_type]} missions\n"
        )


    # TODO: PART 6 - Write the report to file

    rf.write_report_to_file(output_file, report)

    print(f"\nReport created: {output_file}")


# Main execution
if __name__ == '__main__':
    print("Generating squadron activity reports...")

    # Example: Generate report for VFA-41
    generate_squadron_report(
        'VFA-41',
        'reports/vfa-41-report.txt'
    )