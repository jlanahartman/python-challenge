
"""
The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote
"""

import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv, "r") as csvFile:
    csvRead = csv.reader(csvFile, delimiter=",")

    next(csvRead)

    candidates = []
    num_votes = 0
    vote_counts = []


    for row in csvRead:


        num_votes = num_votes + 1

    
        candidate = row[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
    
        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0
#percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
    winner = candidates[max_index]

    #print results
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {num_votes}")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
        print("---------------------------")
        print(f"Winner: {winner}")
        print("---------------------------")

write_file = f"pypoll_results_summary.txt"

#open write file
filewriter = open(write_file, mode = 'w')

#print analysis to file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {num_votes}\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

#close file
filewriter.close()