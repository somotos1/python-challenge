import os
import csv
# Include the path for the csv file
bankdataCSV = os.path.join("..", "/PyPoll", "election_data.csv")
# Open the csv file in read mode
with open('election_data.csv', 'r') as csvfile:
    # set the delimiter as commas
    data = csv.reader(csvfile, delimiter=',')
    next(data)
    pollResults = {}
    vote_count = 0
    current_winner = ''
    highest_vote_percentage = 0
    for row in data:
        vote_count += 1
        name = row[2]
        if name in pollResults.keys():     
            pollResults[name]['vote counts'] += 1
            pollResults[name]['vote percentage'] = (pollResults[name]['vote counts'] / vote_count) * 100
            if pollResults[name]['vote percentage'] > highest_vote_percentage:
                current_winner = name
                highest_vote_percentage = pollResults[name]['vote percentage']
        else:
            pollResults[name] = {'vote counts': 1, 'vote percentage': (1 / vote_count) * 100}
print("Election Results")
print("----------------------------")
print(f"Total votes: {vote_count} ")
print("----------------------------")
for name in pollResults.keys():
    print(f"{name}: {pollResults[name]['vote percentage']:0.3f}% ({pollResults[name]['vote counts']})")
print("----------------------------")
print(f"Winner: {current_winner}")
print("----------------------------")