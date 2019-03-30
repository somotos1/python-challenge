import os
import csv
# Include the path for the csv file
bankdataCSV = os.path.join("..", "/PyPoll", "election_data.csv")
# Open the csv file in read mode
with open('election_data.csv', 'r') as csvfile:
    # set the delimiter as commas
    data = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    next(data)
    # Create empty dictionary for poll results
    pollResults = {}
    # Set vote count to zero for counter
    vote_count = 0
    # Set current winner to empty string
    current_winner = ''
    # set highest vote percentage to zero
    highest_vote_percentage = 0
    # Loop through the data
    for row in data:
        # For each row, add 1 to the vote count
        vote_count += 1
        # set name to the value in index position 2 of each row
        name = row[2]
        # if the name in this row is in pollresults dictionary
        if name in pollResults.keys():
            # add counts to the individuals name and set dictionary value name to 'vote counts'     
            pollResults[name]['vote counts'] += 1
            # set the vote percentage to be equal to the individuals vote count divided by the total votes, convert to percentage; then add 'vote percentage' to dictionary
            pollResults[name]['vote percentage'] = (pollResults[name]['vote counts'] / vote_count) * 100
            # if the vote percentage for this individual is greater than the highest vote percentage
            if pollResults[name]['vote percentage'] > highest_vote_percentage:
                # make the individual the winner
                current_winner = name
                highest_vote_percentage = pollResults[name]['vote percentage']
        # if the individuals name is not in the pollresults dictionary
        else:
            # add the following to the dictionary
            pollResults[name] = {'vote counts': 1, 'vote percentage': (1 / vote_count) * 100}
# save path of file
output_path = os.path.join("..", "python_challenge", "text_script.txt")
# Create a text file and open in write mode
with open("text_script.txt", "w") as text_file:
    
    # Print to text file
    print("Election Results", file=text_file)
    print("----------------------------", file=text_file)
    print(f"Total votes: {vote_count} ", file=text_file)
    print("----------------------------", file=text_file)
    for name in pollResults.keys():
        print(f"{name}: {pollResults[name]['vote percentage']:0.3f}% ({pollResults[name]['vote counts']})", file=text_file)
    print("----------------------------", file=text_file)
    print(f"Winner: {current_winner}", file=text_file)
    print("----------------------------", file=text_file)
# Open the text file in read  mode and print results in terminal
with open("text_script.txt", "r") as text_file2:
    print(text_file2.read())