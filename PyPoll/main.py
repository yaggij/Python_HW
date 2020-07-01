import os
import csv

budget_data_csv = os.path.join("Resources", "PyPoll_Resources_election_data.csv")

votes = 0
candidates = []
vote_count = []

with open(budget_data_csv, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        votes = votes +1
        candidate_in = (row[2])

        if candidate_in in candidates:
            candidate_index = candidates.index(candidate_in)
            vote_count[candidate_index] = vote_count[candidate_index]+1 

        else:
            candidates.append(candidate_in)
            vote_count.append(1)


percent = []
max_votes = vote_count[0]
max_index = 0

for x in range(len(candidates)):
    vote_pct = round(vote_count[x]/votes*100, 2)
    percent.append(vote_pct)

    if vote_count[x] > max_votes:
        max_votes = vote_count[x]
        max_index = x

election_winner = candidates[max_index]


print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
print("--------------------------")
for x in range(len(candidates)):
    print(f"{candidates[x]} : {percent[x]}% ({vote_count[x]})")
print("--------------------------")
print(f"Election Winner: {election_winner.upper()}")
print("--------------------------")



electionfile = os.path.join("pypoll.txt")
with open(electionfile, "w", newline="") as results:
    results.write("Election Results\n")
    results.write("------------------------------")
    results.write(f'Total Votes: {votes}\n')
    results.write("------------------------------")
    for x in range(len(candidates)):
        results.write(f"{candidates[x]} : {percent[x]}% ({vote_count[x]})\n")
    results.write("------------------------------")
    results.write(f"Election Winner: {election_winner.upper()}\n")
    results.write("------------------------------")