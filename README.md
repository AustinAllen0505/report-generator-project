# Flight Operations Report Generator

## Mission Brief

The Operations Officer needs automated reporting capabilities for flight operations data. Currently, all reports are being compiled manually from CSV exports, which is time-consuming and error-prone. Your task is to build a Python-based report generation system that can quickly produce the required operational reports.

## Situation

You've been provided with three CSV data files containing:
- **pilots.csv** - Pilot roster with ranks, experience, and squadron assignments
- **aircraft.csv** - Aircraft inventory with tail numbers, maintenance status, and assignments
- **flight_logs.csv** - Complete flight operations log (2000+ records) with mission details

All files are located in the `data/` directory. Generated reports should be saved to the `reports/` directory.

## Understanding the Data Relationships

The three CSV files are related through **key fields** - specific columns that connect information across files:

```
pilots.csv           flight_logs.csv        aircraft.csv
┌──────────────┐     ┌──────────────┐       ┌──────────────┐
│ pilot_id (PK)│◄────│ pilot_id (FK)│       │aircraft_id(PK)│
│ squadron     │     │ aircraft_id  │──────►│ squadron     │
│ callsign     │     │ mission_type │       │ tail_number  │
│ rank         │     │ duration_hrs │       │ status       │
└──────────────┘     └──────────────┘       └──────────────┘
```

**Key Relationships:**
- **flight_logs.pilot_id** → **pilots.pilot_id**: Links each flight to who flew it
- **flight_logs.aircraft_id** → **aircraft.aircraft_id**: Links each flight to which aircraft was used

**Why this matters:**
- Flight logs store IDs (`P001`, `A005`) instead of full details
- To show pilot names in reports, you need to **join** flight data with pilot data using `pilot_id`
- To show aircraft details, you **join** flight data with aircraft data using `aircraft_id`

**Example:**
```
Flight record: {"flight_id": "FL001", "pilot_id": "P001", "aircraft_id": "A001"}
Pilot record:  {"pilot_id": "P001", "callsign": "Maverick", "rank": "Capt"}
Aircraft record: {"aircraft_id": "A001", "tail_number": "NE-400"}

After joining: {"flight_id": "FL001", "pilot_id": "P001", "callsign": "Maverick",
                "rank": "Capt", "aircraft_id": "A001", "tail_number": "NE-400"}
```

This is exactly what your `join_data()` function will accomplish in Phase 3.

## Tasking

### Phase 1: Data Access Foundation

**REQUIREMENT:** Build a Python module (`report_functions.py`) that can read and process the CSV data files.

Command needs the ability to:
- Load CSV files into memory for processing
- Count total records in any dataset
- Extract unique values from any field (e.g., list all mission types)
- Filter records by specific criteria (e.g., all flights by a specific pilot)

### Phase 2: Statistical Analysis

**REQUIREMENT:** Implement functions to calculate operational statistics.

Operations wants to be able to:
- Calculate total values for numeric fields (total flight hours, total fuel consumption)
- Calculate average values (average mission duration, average fuel usage)
- Look up specific records by ID (find pilot by pilot_id, find aircraft by tail number)

### Phase 3: Cross-Reference Capability

**REQUIREMENT:** Build the ability to combine data from multiple sources.

Intelligence needs to:
- Match flights with pilot information (who flew each mission)
- Match flights with aircraft information (which aircraft flew each mission)
- Generate enriched datasets that include related information from multiple files

### Phase 4: Report Generation

**REQUIREMENT:** Create formatted text reports and write them to files.

Command requires:
- Clean, formatted text output
- Professional headers and section breaks
- Reports saved as text files for distribution
- Ability to generate reports on demand for any squadron

### Phase 5: Squadron Activity Report (Main Deliverable)

**REQUIREMENT:** Using all the functions built in Phases 1-4, create a script that generates comprehensive squadron activity reports.

The Operations Officer needs a report for each squadron that includes:
- Squadron personnel roster (all assigned pilots)
- Squadron aircraft inventory (all assigned aircraft)
- Total flight hours for the squadron
- Total number of missions flown
- Breakdown of missions by type (Training, Patrol, Combat, etc.)
- Average mission duration
- Current operational status

**Format:** The report must be professional, well-organized, and saved as a text file.

**Deliverable:** `generate_squadron_report.py` script that accepts a squadron code and produces the required report.

## Acceptance Criteria

Your report generator will be evaluated based on:
- ✅ All required functions implemented and tested
- ✅ Squadron reports generate successfully for all squadrons
- ✅ Reports contain accurate calculations
- ✅ Output files are well-formatted and readable
- ✅ Code is modular and reusable
- ✅ Functions include proper documentation

## Additional Tasking (If Time Permits)

If you complete the primary requirements ahead of schedule, Operations has additional reporting needs:

- **Pilot Performance Reports** - Individual pilot activity summaries
- **Aircraft Utilization Reports** - Flight hours and maintenance status by tail number
- **Mission Type Analysis** - Detailed breakdown of operations by mission type
- **Fuel Efficiency Reports** - Fuel consumption analysis across squadrons
- **Date Range Reports** - Activity reports for specific time periods
- **CSV Output** - Option to export reports in CSV format for spreadsheet analysis

## Getting Started

1. Review the data files in the `data/` directory to understand the available information
2. Start with `report_functions.py` - implement and test each function individually
3. Test your functions using the code block at the bottom of `report_functions.py`
4. Once your functions are working, move to `generate_squadron_report.py`
5. Implement the squadron report generator step by step
6. Test with multiple squadrons to verify accuracy

## Resources

- Data files: `data/pilots.csv`, `data/aircraft.csv`, `data/flight_logs.csv`
- Function module: `src/report_functions.py`
- Report generator: `src/generate_squadron_report.py`
- Output directory: `reports/` (create this directory before running your scripts)

## Notes

This is a realistic workflow you'll encounter in operational environments. Data comes in various formats (often CSV exports from other systems), and you'll need to write custom tools to process and report on that data. The skills you build here - reading files, processing data, calculating statistics, and generating reports - are directly applicable to real-world military and civilian roles.

Make incremental progress. Test each function as you build it. Ask for help when you're stuck. Outstanding work often comes from outstanding debugging skills.

---

**Mission Start:** Ready when you are.
**Expected Completion:** See your Learn module for timeline guidance.
**Point of Contact:** Your instructor for technical support.
