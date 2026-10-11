"""
RECORD CHECK  -  my version
===========================

Name  : Rayyan Moosa
Lane  :  IT
Date  : 2026-10-01

Run it:   python template.py
"""

# EXCELLENT TIER: Variable to keep track of OVER LIMIT records outside the loop
over_limit_count = 0

# EXCELLENT TIER: Wrap everything in a loop
while True:
    # ==================================================================== INPUT
    # 1. Ask for your three values.
    
    label = input("Enter hostname (or 'quit' to stop): ")
    
    # Check if the user wants to quit before asking for the numbers
    if label.lower() == "quit":
        break
        
    value = float(input("Enter GB used: "))
    limit = float(input("Enter GB total: "))


    # ================================================================== PROCESS
    # 2. Work out the difference and the percentage.       [Typical and above]
    
    difference = limit - value   
    percent = (value / limit) * 100      
    
    # 3. Decide a status and store it in a variable called status.
    #    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
    #                                     "WARNING" (90% or more), otherwise "OK"
    
    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1  # Add 1 to our running total
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"


    # =================================================================== OUTPUT
    # 4. Print the report.
    #    Typical   : add difference and percent, 2 decimal places, right-aligned
    
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Free        : {difference:>10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()

# ==========================================================================
# EXCELLENT TIER: Print the final count after the loop ends
print(f"Session finished. Total records OVER LIMIT: {over_limit_count}")

# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds