

import os
import csv 

csvpath = os.path.join("Resources", "election_data.csv")

total_votes = []
past_id = 0
winning_vote = 0

with open(csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader)

	for votes in csvreader:
		voter_id = votes[0]
		candidate = votes[2]
		if voter_id != past_id:
			total_votes.append(candidate)
			past_id = voter_id
	kcount = total_votes.count("Khan")
	ccount = total_votes.count("Correy")
	lcount = total_votes.count("Li")
	ocount = total_votes.count("O'Tooley")
	total = len(total_votes)

	final = {"Khan": kcount, "Correy": ccount, "Li": lcount, "O'Tooley": ocount}
	for candidate, vote_calc in final.items():
		if vote_calc > winning_vote:
			winning_vote = vote_calc
			winner = candidate

def percent (votes, total):
	return (votes/total)*100

print("Election Results")
print("----------------------------")
print(f'Total Votes: {total}')
print("----------------------------")
print(f'Khan: {round(percent(kcount,total), 3)}%  ({kcount})')
print(f'Correy: {round(percent(ccount, total), 3)}%  ({ccount})')
print(f'Li: {round(percent(lcount, total), 3)}%  ({lcount})')
print(f"O'Tooley: {round(percent(ocount, total), 3)}%  ({ocount})")
print("----------------------------")
print(f'Winner: {winner}')
print("----------------------------")

output_path = os.path.join("Election Results.csv")

with open(output_path, "w", newline="") as csvfile:
	new = csv.writer(csvfile, delimiter=",")

	new.writerow(["Election Results"])
	new.writerow(["----------------------------"])
	new.writerow([f'Total Votes: {total}'])
	new.writerow(["----------------------------"])
	new.writerow([f'Khan: {round(percent(kcount,total), 3)}%  ({kcount})'])
	new.writerow([f'Correy: {round(percent(ccount, total), 3)}%  ({ccount})'])
	new.writerow([f'Li: {round(percent(lcount, total), 3)}%  ({lcount})'])
	new.writerow([f"O'Tooley: {round(percent(ocount, total), 3)}%  ({ocount})"])
	new.writerow(["----------------------------"])
	new.writerow([f'Winner: {winner}'])
	new.writerow(["----------------------------"])
	