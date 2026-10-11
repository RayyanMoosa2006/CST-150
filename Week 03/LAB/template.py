"""
RECORD CHECK - my version
===========================

Name : Rayyan Moosa
Lane : AI
Date : 05 October 2026

Run it: python template.py
"""

def status_of(percent):
    """Return the status for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the record check report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Rows loaded : {value:10.2f}")
    print(f"  Expected    : {limit:10.2f}")
    print(f"  Difference  : {difference:10.2f}")
    print(f"  Percent     : {percent:10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


over_count = 0

while True:
    label = input("Dataset name (or quit): ")
    if label == "quit":
        break

    value = float(input("Rows loaded: "))
    limit = float(input("Rows expected: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_count = over_count + 1

print("Records over limit:", over_count)