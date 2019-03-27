import os
import csv
# Include the path for the csv file
# bankdataCSV = os.path.join("..", "/PyPoll", "election_data.csv")
# Open the csv file in read mode
with open('election_data.csv', 'r') as csvfile:
    # set the delimiter as commas
    data = csv.reader(csvfile, delimiter=',')
    next(data)
    vote_count = 0
    votes_for_candidate1 = 0
    votes_for_candidate2 = 0
    votes_for_candidate3 = 0
    votes_for_candidate4 = 0
    candidateSet = set()
    for row in data:
        vote_count += 1
        candidateSet.add(row[2])
        candidateList = list(candidateSet)
        if row[2] == candidateList[0]:
            votes_for_candidate1 += 1
        elif row[2] == candidateList[1]:
            votes_for_candidate2 += 1
        elif row[2] == candidateList[2]:
            votes_for_candidate3 += 1
        elif row[2] == candidateList[3]:
            votes_for_candidate4 += 1
    candidate1percent = votes_for_candidate1 / vote_count
    candidate2percent = votes_for_candidate2 / vote_count
    candidate3percent = votes_for_candidate3 / vote_count
    candidate4percent = votes_for_candidate4 / vote_count
    print(f"Total votes: {vote_count} ")
    print(f"{candidateList[0]}: {(candidate1percent * 100):0.3f}% ({votes_for_candidate1})")
    print(f"{candidateList[1]}: {(candidate2percent * 100):0.3f}% ({votes_for_candidate2})")
    print(f"{candidateList[2]}: {(candidate3percent * 100):0.3f}% ({votes_for_candidate3})")
    print(f"{candidateList[3]}: {(candidate4percent * 100):0.3f}% ({votes_for_candidate4})")
    if candidate1percent > candidate2percent and candidate1percent > candidate3percent and candidate1percent > candidate4percent:
        print(f"Winner: {candidateList[0]}")
    if candidate2percent > candidate1percent and candidate2percent > candidate3percent and candidate2percent > candidate4percent:
        print(f"Winner: {candidateList[1]}")
    if candidate3percent > candidate1percent and candidate3percent > candidate2percent and candidate3percent > candidate4percent:
        print(f"Winner: {candidateList[2]}")
    if candidate4percent > candidate2percent and candidate4percent > candidate3percent and candidate4percent > candidate1percent:
        print(f"Winner: {candidateList[3]}")