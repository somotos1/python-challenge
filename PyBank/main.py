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
        # If the current amount - previous amount result is greater than current max increase set max inc amount and date
        if (current_amount - previous_amount) > current_max_inc:
            current_max_inc = (current_amount - previous_amount)
            current_max_inc_date = row[0]
        elif (current_amount - previous_amount) < current_max_inc:
            pass
        # If the current amount - previous amount result is greater than current max decrease set max dec amount and date
        if (current_amount - previous_amount) < current_max_dec:
            current_max_dec = (current_amount - previous_amount)
            current_max_dec_date = row[0]
        elif (current_amount - previous_amount) > current_max_dec:
            pass
        previous_amount = current_amount

# Save path of file
output_path = os.path.join("..", "python_challenge", "budget_script.txt")
# Open file in write mode
with open("budget_script.txt", "w") as text_file:
    
    # print the following in the text file
    print(f"Total months: {(len(unique_months))}", file=text_file)
    print(f"Total: ${net_total}", file=text_file)
    print(f"Average change: ${chg_sum/(row_count-1):0.2f}", file=text_file)
    print(f"Greatest increase in profits: {current_max_inc_date} ($ {str(current_max_inc)} )", file=text_file)
    print(f"Greatest decrease in profits: {current_max_dec_date} ($ {str(current_max_dec)} )", file=text_file)

# Open the text file in read  mode and print results in terminal
with open("budget_script.txt", "r") as text_file2:
    print(text_file2.read())