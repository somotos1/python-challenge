import os
import csv
# Include the path for the csv file
bankdataCSV = os.path.join("..", "/PyBank", "budget_data.csv")
# Open the csv file in read mode
with open('budget_data.csv', 'r') as csvfile:
    # set the delimiter as commas
    data = csv.reader(csvfile, delimiter=',')
    
    # Skip the first line with header info
    next(data)
    # Create an empty set to count the number of unique months (check for duplicate months)
    unique_months = set()
    # set variable for net total results as counter
    net_total = 0
    # set variable for average change results
    chg_sum = 0
    row_count = 0
    # Set the previous amount to 'none' to account for no comparison against row 1
    previous_amount = None
    # Set the current maximum increase and decrease to be zero as a starting point
    current_max_inc = 0
    current_max_dec = 0
    # include variable for current maximum inc/dec dates
    current_max_inc_date = ""
    current_max_dec_date = ""
    # Loop through each row in the dataset
    for row in data:
        row_count += 1
        # Get a unique list of months and add to a set
        unique_months.add(row[0])
        # Sum the profits and losses column
        net_total = net_total + int(row[1])
        # Set the current amount to be the row we are iterating over and in index 1 position
        current_amount = (int(row[1]))
        # If previous amount is none, set previous amount and continue
        if previous_amount is None:
            previous_amount = (int(row[1]))
            # go to the next row if previous amount is none
            continue
        chg_sum = chg_sum + (current_amount - previous_amount)
        # If the current amount - previous amount result is greater than current max increase
        if (current_amount - previous_amount) > current_max_inc:
            current_max_inc = (current_amount - previous_amount)
            current_max_inc_date = row[0]
        elif (current_amount - previous_amount) < current_max_inc:
            pass
        if (current_amount - previous_amount) < current_max_dec:
            current_max_dec = (current_amount - previous_amount)
            current_max_dec_date = row[0]
        elif (current_amount - previous_amount) > current_max_dec:
            pass
        previous_amount = current_amount
    print(f"Total months: {(len(unique_months))}")
    print(f"Total: ${net_total}")
    print(f"Average change: ${chg_sum/(row_count-1):0.2f}")
    print(f"Greatest increase in profits: {current_max_inc_date} ($ {str(current_max_inc)} )")
    print(f"Greatest decrease in profits: {current_max_dec_date} ($ {str(current_max_dec)} )")