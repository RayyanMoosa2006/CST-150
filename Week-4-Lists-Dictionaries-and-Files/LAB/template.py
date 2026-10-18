
"""
RECORD CHECK  -  my version
===========================

Name  : Rayyan Moosa
Lane  : AI & Data Science
Date  : 18/10/2026

Run it:   python template.py
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

def check_record(value, limit):
    """Check a value and return its results."""
    difference = value - limit
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value=0, limit=0, difference=0, percent=0, status="", total_over=None):
    """Print a record report or the final total."""
    if total_over is not None:
        print("Total records over limit:", total_over)
    else:
        print("Record:", label)
        print("Value:", value)
        print("Limit:", limit)
        print("Difference:", difference)
        print("Percent:", round(percent, 1), "%")
        print("Status:", status)
        print()


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path):
    """Read records from a file into a list of dictionaries."""
    records = []

    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                record = {
                    "label": parts[0],
                    "value": float(parts[1]),
                    "limit": float(parts[2])
                }
                records.append(record)

    return records


records = load_records("records.txt")


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

total_over = 0

with open("results.txt", "w") as file:
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])

        print_report(record["label"], record["value"], record["limit"],
                     difference, percent, status)

        file.write(record["label"] + "," + status + "\n")

        if status == "OVER LIMIT":
            total_over += 1

print_report("Total", total_over=total_over)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
